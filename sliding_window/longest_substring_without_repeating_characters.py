"""
Problem No. 3

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        l = 0
        maxlen = 0
        
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            maxlen = max(maxlen, (r-l+1)) #bc array is 0 indexed

        return maxlen

        """
        longest = 0
        substring = ""
        l = 0
        r = 1

        substring += s[l]

        while r < len(s):
            if s[r] in substring:
                #restart
                l = r
            else:
                substring += s[r]
                print(substring)
                length = r-1
                longest = max(length, longest)
            r += 1

        return longest
        """