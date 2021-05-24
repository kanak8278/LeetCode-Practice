# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def pathSumUtility(root, targetSum):
            if root is None:
                return False
            else:
                node = root
                result = False
                subSum = targetSum - node.val

                if subSum == 0 and node.left is None and node.right is None:
                    return True

                if node.left is not None:
                    result = result or pathSumUtility(node.left, subSum)
                if node.right is not None:
                    result = result or pathSumUtility(node.right, subSum)
                return result

        return pathSumUtility(root, targetSum)
