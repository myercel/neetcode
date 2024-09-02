"""
Problem No. 242

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        s = sorted(s)
        t = sorted(t)

        return s == t

        """
        if len(s) != len(t):
            return False
            
        hashs = {}
        hasht = {}
        for i in range(len(s)):
            hashs[s[i]] = 1 + hashs.get(s[i], 0)
            hasht[t[i]] = 1 + hasht.get(t[i], 0)

    
        return hashs == hasht