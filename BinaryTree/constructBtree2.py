# Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helpBuild(preorder, inorder):
            if len(preorder) != len(inorder) and len(preorder) == 0 and len(inorder) == 0:
                return None
            root = preorder[0]

            idx = self.find(inorder, root)

            root_node = TreeNode(val=root)

            left_preorder = preorder[1:idx + 1]
            right_preorder = preorder[idx + 1:]

            left_inorder = inorder[:idx]
            right_inorder = inorder[idx + 1:]

            if left_preorder and left_inorder:
                root_node.left = helpBuild(left_preorder, left_inorder)
            else:
                root_node.left = None
            if right_preorder and right_inorder:
                root_node.right = helpBuild(right_preorder, right_inorder)
            return root_node

        return helpBuild(preorder, inorder)

    def find(self, num_list: List[int], num):
        for idx, _ in enumerate(num_list):
            if num_list[idx] == num:
                return idx
