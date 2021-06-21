import math


class Stack:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False

    def push(self, element):
        self.arr.append(element)

    def pop(self):
        if self.isEmpty():
            return

        return self.arr.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.arr[-1]


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = Stack()
        self.MinStack = Stack()

    def push(self, val: int) -> None:
        self.stack.push(val)
        if self.MinStack.isEmpty():
            self.MinStack.push(val)

        else:
            if self.MinStack.top() >= val:
                self.MinStack.push(val)

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.MinStack.top():
            self.MinStack.pop()

    def top(self) -> int:
        return self.stack.top()

    def getMin(self) -> int:
        return self.MinStack.top()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()