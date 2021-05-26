# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.nc = 0

    def levelOrderTraversal(self, root):
        # l = []
        lst = []
        queue = []
        queue.append(root)
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)

                if node is None:
                    lst.append(None)
                    # lst.append(None)
                    continue
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)

            # l.append(lst)
        return lst

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        l = self.levelOrderTraversal(root)
        # print(l)
        return l

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        queue = []
        x = data.pop(0)
        if x is None:
            return
        root = TreeNode(x)
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node is None:
                    continue
                if len(data) == 0:
                    break
                l = data.pop(0)
                y = data.pop(0)

                if l is not None:
                    node.left = TreeNode(l)
                    queue.append(node.left)

                if y is not None:
                    node.right = TreeNode(y)
                    queue.append(node.right)
        return (root)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))