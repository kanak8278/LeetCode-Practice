# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        current2 = head
        current1 = head
        if head is None:
            return False
        while current1.next != None and current1.next.next != None and current2.next != None and current2.next.next != None:
            current1 = current1.next
            current2 = current2.next.next
            if current1 == current2:
                return True
        return False
