import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
         self.random = random



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        current = head
        new_head = copy.deepcopy(head)
        new_current = new_head

        while current is not None:
            next = current.next
            current.next = new_current

            new_current.next = copy.deepcopy(next)
            new_current.random = current

            current = next
            new_current = new_current.next

        current = head
        new_current = new_head
        while new_current is not None:
            random = new_current.random.random
            new_current.random = random.next
            new_current = new_current.next
        return new_head




