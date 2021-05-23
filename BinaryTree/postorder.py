"""
# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)
            l.append(root.val)
        traverse(root)
        return l
"""

