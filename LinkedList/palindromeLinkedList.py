# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = list()
        current = head
        while current is not None:
            l.append(current.val)
            current = current.next

        for idx, element in enumerate(l):
            if l[idx] != l[len(l) - idx - 1]:
                return False
        return True


