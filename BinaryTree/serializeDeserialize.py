# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
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
        root = TreeNode(data[0])
        idx = 0
        none_count = 0
        queue.append((idx, root))
        idx += 1
        while queue:
            for _ in range(len(queue)):
                index, node = queue.pop(0)
                if node is None:
                    none_count += 1
                    continue
                node.left = TreeNode(data[2 * index + 1 - 2 * none_count])
                node.right = TreeNode(data[index * 2 + 2 - 2 * none_count])

                queue.append((idx, node.left))
                idx += 1
                queue.append((idx, node.right))
                idx += 1
                print(queue)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))