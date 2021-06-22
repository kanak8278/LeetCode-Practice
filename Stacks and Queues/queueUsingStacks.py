from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        ele = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return ele

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        ele = self.s2.pop()
        self.s2.append(ele)
        while self.s2:
            self.s1.append(self.s2.pop())
        return ele

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.s1) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()