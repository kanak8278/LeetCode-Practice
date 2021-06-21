from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for p in s:
            print(p)
            if len(stack) == 0 and (p == "]" or p == "}" or p == ")"):
                return False
            if p == "{" or p == "[" or p == "(":
                stack.append(p)
            if p == "}":
                e = stack.pop()
                if e == "{":
                    continue
                else:
                    return False
            if p == "]":
                e = stack.pop()
                if e == "[":
                    continue
                else:
                    return False
            if p == ")":
                e = stack.pop()
                if e == "(":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
