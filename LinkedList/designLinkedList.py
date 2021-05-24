class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for x in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            prev_head = self.head
            self.head = node
            self.head.next = prev_head
            prev_head.prev = self.head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head
        node = Node(val)
        if current is None:
            self.head = node
        else:
            for i in range(self.size - 1):
                current = current.next
            current.next = node
            node.prev = current

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next

            node = Node(val)
            node.prev = curr
            node.next = curr.next
            curr.next = node
            if node.next is not None:
                node.next.prev = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            if current.next.next is None:
                current.next = None
            else:
                current.next = current.next.next
                current.next.prev = current

        self.size -= 1

    # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)