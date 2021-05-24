# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        current = head
        if current is None:
            return None

        s = set()
        while current not in s:
            s.add(current)
            current = current.next
            if current is None:
                return None
        return current
        # index = 0
        # while head !=  current:
        #     head = head.next
        #     index+=1
        # return