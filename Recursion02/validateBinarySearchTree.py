# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, low, high):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            else:
                # print(low, high)
                return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, -math.inf, math.inf)
