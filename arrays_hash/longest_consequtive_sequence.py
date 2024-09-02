"""
Problem No. 128

Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
    Therefore its length is 4.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # check if start of a sequence
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

        """
        # Two pointers
        nums.sort()
        print(nums)

        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        l = 0
        r = 1
        max_length = 0

        while r < len(nums):
            print(l, r)
            if nums[r] == nums[r-1]:
                r += 1
            else:
                l = r
                r += 1
            max_length = max(max_length, (r-l))

        return max_length
        """