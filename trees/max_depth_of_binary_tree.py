"""
Problem No. 104

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # My solution - recursive DFS formula
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        """
        # BFS
        if not root:
            return 0
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft() # or q.pop()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                print("****" , q)
            level += 1
        return level
        """
        """
        # Iterative DFS
        stack = [[root, 1]]
        maxdepth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                maxdepth = max(maxdepth, depth)
                stack.append([node.left, 1 + depth])
                stack.append([node.right, 1 + depth])

        return maxdepth
        """