"""
Problem No. 124

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in 
the sequence has an edge connecting them. A node can only appear in the sequence at 
most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            leftmax = max(leftmax, 0)
            rightmax = dfs(root.right)
            rightmax = max(rightmax, 0)

            res[0] = max(res[0], (root.val + leftmax + rightmax))

            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        return res[0]