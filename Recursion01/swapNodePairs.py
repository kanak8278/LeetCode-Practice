# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        def utility(prev, node):
            if node is None or node.next is None:
                return node
            # print(node.val)
            nxt = node.next
            nxt2nxt = node.next.next
            nxt.next = node
            node.next = nxt2nxt
            if prev is not None:
                prev.next = nxt
            prev = node
            # print(node.val, nxt.val)
            utility(prev, nxt2nxt)
            return nxt
        return utility(prev, head)