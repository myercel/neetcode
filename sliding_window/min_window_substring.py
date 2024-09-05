"""
Problem No. 76

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # edge case: t is empty
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        ans, anslen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r-l+1) < anslen:
                    ans = [l, r]
                    anslen = (r-l+1)

                # pop from the left side of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = ans
        return s[l: r+1] if anslen != float("inf") else ""

        """
        # edge case: t is longer than s
        if len(t) > len(s):
            return ""

        l = 0
        r = 0
        tset = set()
        min_length = float('inf')
        ans = ""

        for c in t:
            tset.add(c)

        while r < len(s) - 1:
            length = r - l
            
            if s[r] in tset:
                tset.remove(s[r])
                ans += s[r]

            elif length > min_length:
                l = r
            r+= 1
            
        return ans
        """