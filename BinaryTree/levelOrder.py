# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        l = []
        queue = []
        if root:
            queue.append(root)

        while queue:
            # l.append(queue)
            # print()
            level = []
            ln = len(queue)
            for i in range(ln):
                # print(queue)
                # print(len(queue))
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            l.append(level)
        return l
