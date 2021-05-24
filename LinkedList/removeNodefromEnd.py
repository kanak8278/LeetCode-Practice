# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = self.getSize(head)
        current = head

        if n == size:
            head = head.next
            return head
        m = size - n

        for _ in range(m - 1):
            current = current.next
        current.next = current.next.next
        return head

    def getSize(self, head: ListNode):
        size = 0
        while head is not None:
            head = head.next
            size += 1
        return size
