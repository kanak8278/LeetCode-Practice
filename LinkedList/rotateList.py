# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        tail, size = self.getSize(head)
        k = k % size
        if k == 0:
            return head

        n = size - k
        current = head
        for _ in range(n - 1):
            current = current.next
        new_head = current.next
        current.next = None
        tail.next = head
        return new_head

    def getSize(self, head: ListNode):
        current = head
        size = 0
        while current.next is not None:
            current = current.next
            size += 1
        return current, size + 1
