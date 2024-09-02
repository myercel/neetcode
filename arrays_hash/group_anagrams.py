"""
Problem No. 49

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            ans[tuple(count)].append(s)

        return ans.values()
        """
        # My solution:
        # have a dictionary that stores sort(word) : [words that have same sorting]
        hashmap = {}

        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in hashmap:
                hashmap[sort] = [string]
            else:
                hashmap[sort].append(string)

        return hashmap.values()