# Construct Binary Tree from Inorder and Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def buildhelper(inorder, postorder):
            if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
                return

            root = postorder[-1]
            root_node = TreeNode(val=root)
            idx = self.find(num_list=inorder, num=root)
            # print(idx)

            left_branch = inorder[:idx]
            right_branch = inorder[idx + 1:]
            left_postorder = postorder[:idx]
            right_postorder = postorder[idx:-1]

            if left_branch and left_postorder:
                root_node.left = buildhelper(left_branch, left_postorder)
            else:
                root_node.left = None

            if right_branch and right_postorder:
                root_node.right = buildhelper(right_branch, right_postorder)
            else:
                root_node.right = None
            return root_node

        return buildhelper(inorder, postorder)

    def find(self, num_list: List[int], num):
        for idx, _ in enumerate(num_list):
            if num_list[idx] == num:
                return idx
