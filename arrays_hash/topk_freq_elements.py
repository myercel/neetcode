"""
Problem No. 347

Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            """
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            """
        for n, c in count.items(): # returns key,value pairs
            freq[c].append(n)

        ans = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans