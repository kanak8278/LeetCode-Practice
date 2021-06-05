# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def utility(root, depth):
            if root is None:
                return depth
            return max(utility(root.left, depth + 1), utility(root.right, depth + 1))

        return utility(root, 0)
