# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        while head != None and head.val == val:
            head = head.next
        if head is None:
            return head

        prev = head
        current = head.next

        while current is not None:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        return head



