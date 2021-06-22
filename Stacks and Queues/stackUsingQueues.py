from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        ele = self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        return ele

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        ele = self.q1.popleft()
        self.q2.append(ele)
        while self.q2:
            self.q1.append(self.q2.popleft())
        return ele

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q1) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()