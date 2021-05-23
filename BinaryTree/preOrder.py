# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
# Recursive Solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def traverse(root):
            if root is None:
                return
            l.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return l
"""


"""
# Iterative Solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        l = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node is not None:
                l.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return l
"""


