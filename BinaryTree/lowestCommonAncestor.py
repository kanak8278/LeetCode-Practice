# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        visit_p = False
        visit_q = False
        parent = self.Traversal(root)
        p_set = set()
        q_set = set()

        node = p
        while node:
            p_set.add(node)
            node = parent[node]

        node = q
        while node:
            q_set.add(node)
            node = parent[node]

        intersection = p_set.intersection(q_set)
        node = p

        while node:
            if node in intersection:
                break
            node = parent[node]

        return node

    def Traversal(self, root):
        parent = {}
        parent[root] = None

        def dfs(root):
            if root is None:
                return
            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)

        dfs(root)
        return parent






