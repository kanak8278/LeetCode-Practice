# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        def utility(prev, curr):
            if curr is None:
                return prev
            nxt = curr.next
            curr.next = prev

            prev = curr
            return utility(prev, nxt)

        return utility(prev, head)


