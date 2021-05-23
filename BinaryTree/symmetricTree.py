# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.Traversal1(root.left)
        right = self.Traversal2(root.right)
        print(left, right)

        if left == right:
            return True
        else:
            return False

    def Traversal1(self, root: TreeNode):
        l = []

        def dfs(root):
            if root:
                l.append(root.val)
                dfs(root.left)
                dfs(root.right)
            if root is None:
                l.append(root)
                return

        dfs(root)
        return l

    def Traversal2(self, root: TreeNode):
        l = []

        def dfs(root):
            if root:
                l.append(root.val)
                dfs(root.right)
                dfs(root.left)
            if root is None:
                l.append(root)
                return

        dfs(root)
        return l
