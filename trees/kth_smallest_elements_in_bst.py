"""
Problem No. 230

Given the root of a binary search tree, and an integer k, return the 
kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            curr = curr.right