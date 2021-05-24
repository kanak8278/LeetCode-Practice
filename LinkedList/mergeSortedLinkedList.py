# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        currA = l1
        currB = l2

        if currA is None:
            return currB
        if currB is None:
            return currA

        head = None
        l = []
        while currA is not None and currB is not None:
            while currB is not None and currA is not None and currA.val >= currB.val:
                l.append(currB)
                currB = currB.next
            while currA is not None and currB is not None and currA.val <= currB.val:
                l.append(currA)
                currA = currA.next
        if currA is None:
            l.append(currB)
        if currB is None:
            l.append(currA)

        head = l[0]
        current = head
        for x in l[1:]:
            current.next = x
            current = x
        return head

