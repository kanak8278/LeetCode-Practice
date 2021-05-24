# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        carry = 0
        l = []
        while True:
            if curr1 is not None and curr2 is not None:
                sum = (curr1.val + curr2.val + carry) % 10
                carry = int((curr1.val + curr2.val + carry) / 10)
                l.append(sum)
                curr1 = curr1.next
                curr2 = curr2.next
            if curr1 is None and curr2 is not None:
                sum = (curr2.val + carry) % 10
                carry = int((curr2.val + carry) / 10)
                l.append(sum)
                curr2 = curr2.next
            if curr2 is None and curr1 is not None:
                sum = (curr1.val + carry) % 10
                carry = int((curr1.val + carry) / 10)
                l.append(sum)
                curr1 = curr1.next
            if curr1 is None and curr2 is None:
                if carry is not 0:
                    l.append(carry)
                break

        head = ListNode(l[0])
        current = head

        for x in l[1:]:
            node = ListNode(x)
            current.next = node
            current = node
        return head






