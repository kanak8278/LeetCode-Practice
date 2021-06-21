from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        next_warmer = []
        for idx in range(len(temperatures) - 1, -1, -1):
            nxt = 0
            while stack:
                ele = stack[-1]
                # print(ele)
                if ele[1] > temperatures[idx]:
                    stack.append((idx, temperatures[idx]))
                    nxt = ele[0] - idx
                    next_warmer.append(nxt)
                    break
                else:
                    stack.pop()
            if nxt == 0:
                if len(stack) == 0:
                    stack.append((idx, temperatures[idx]))
                    next_warmer.append(nxt)
        return (next_warmer[::-1])









