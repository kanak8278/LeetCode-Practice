"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        while current is not None:
            if current.child:
                start, end = self.end_points(current.child)
                # return self.flatten(current.child)
                nxt = current.next
                current.next = start
                start.prev = current
                if nxt is not None:
                    nxt.prev = end
                end.next = nxt
                current.child = None
                current = current.next

            else:
                current = current.next
        return head

    def end_points(self, head: 'Node'):
        current = head

        while current.next is not None:
            current = current.next
        return head, current

