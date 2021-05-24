# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        currentA = headA
        currentB = headB

        sizeA = self.getSize(headA)
        sizeB = self.getSize(headB)

        if sizeA == sizeB:
            return self.checkSame(currentA, currentB)

        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                currentA = currentA.next
            return self.checkSame(currentA, currentB)

        if sizeB > sizeA:
            for _ in range(sizeB - sizeA):
                currentB = currentB.next
            return self.checkSame(currentA, currentB)

    def getSize(self, headA: ListNode) -> int:
        sizeA = 0
        currentA = headA
        while currentA is not None:
            currentA = currentA.next
            sizeA += 1
        return sizeA

    def checkSame(self, headA: ListNode, headB: ListNode):
        currentA = headA
        currentB = headB

        while currentA is not None:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None



