"""
Problem No. 125

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -=1

            elif not s[l].isalnum():
                l += 1
            
            elif not s[r].isalnum():
                r -= 1

        return True

        """
        My OG solution:
        string = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                string += s[i].lower()
        print(string)

        l = 0
        r = len(string) - 1
        while l <= r:

            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
        """

        """
        Alternate solution:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
        """