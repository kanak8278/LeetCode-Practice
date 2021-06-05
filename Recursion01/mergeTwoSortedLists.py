# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is not None and l2 is None:
            return l1
        if l2 is not None and l1 is None:
            return l2
        if l1.val <= l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next

        def utility(root, l1, l2):
            if l1 is None and l2 is not None:
                prev = root
                root.next = l2
                return root
            if l2 is None and l1 is not None:
                prev = root
                root.next = l1
                return root
            if l1 is None and l2 is None:
                prev = root
                root.next = None
                return
            else:
                if l1.val <= l2.val:
                    root.next = l1
                    l1 = l1.next
                    prev = root
                    root = root.next
                    utility(root, l1, l2)
                else:
                    root.next = l2
                    l2 = l2.next
                    prev = root
                    root = root.next
                    utility(root, l1, l2)
                return prev

        return utility(root, l1, l2)
