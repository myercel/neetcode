"""
Problem No. 98

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS formula

        def valid(root, left, right):
            if not root:
                return True
            
            if not (left < root.val and right > root.val):
                return False

            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        
        return valid(root, float("-inf"), float("inf"))

        """
        if not root:
            return True
        if root.left and root.right:
            if root.left.val < root.val and root.right.val > root.val:
                return True
        elif root.left and root.left.val < root.val:
            return True
        elif root.right and root.right.val > root.val:
            return True
        else:
            return False

        return (self.isValidBST(root.left) and self.isValidBST(root.right))
        """