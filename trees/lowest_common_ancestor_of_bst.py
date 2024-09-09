"""
Problem No. 235

Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both 
p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val < curr.val and q.val > curr.val or q.val < curr.val and p.val > curr.val:
                return curr
            if p.val == curr.val or q.val == curr.val:
                return curr
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        """
        if not root:
            return None

        if p.val < root.val and q.val > root.val or q.val < root.val and p.val > root.val:
            return root
        
        if root.val == p.val or root.val == q.val:
            if root.left == p.val or root.left == q.val or root.right == p.val or root.right == q.val:
                return root

        return (self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q))
        """