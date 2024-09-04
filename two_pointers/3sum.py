"""
Problem No. 15

Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                numsum = num + nums[l] + nums[r]
                if numsum > 0:
                    r -= 1
                elif numsum < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return ans

        """
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            while l < r:
                numssum = nums[i] + nums[l] + nums[r]
                if numssum == 0 and [i, l, r] not in ans:
                    ans.append([i, l, r])
                    l += 1
                    r -= 1
                elif numssum > 0:
                    r -= 1
                else:
                    l += 1

        print(ans)
        return ans
        """