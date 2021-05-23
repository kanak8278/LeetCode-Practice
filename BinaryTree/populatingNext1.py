# Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

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
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            l.append(level)
        return l
    def connect(self, root: 'Node') -> 'Node':
        level_list = self.levelOrder(root)

        for idx, _ in enumerate(level_list):
            for idxx, _ in enumerate(level_list[idx]):
                if idxx == len(level_list[idx])-1:
                    level_list[idx][idxx].next = None
                else:
                    level_list[idx][idxx].next = level_list[idx][idxx+1]
        return root


