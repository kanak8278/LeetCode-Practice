from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()

        def moveUp(s, idx):
            l = list(s)
            if l[idx] == "9":
                l[idx] = "0"
            else:
                l[idx] = str(int(l[idx]) + 1)
            return ''.join(l)

        def moveDown(s, idx):
            l = list(s)
            if l[idx] == "0":
                l[idx] = "9"
            else:
                l[idx] = str(int(l[idx]) - 1)
            return ''.join(l)

        def fn(currentStr, turns):
            if currentStr == target:
                return turns
            if currentStr in deadends:
                return
            else:
                for idx in range(4):
                    upString = moveUp(currentStr, idx)
                    downString = moveDown(currentStr, idx)
                    if upString == target or downString == target:
                        return turns+1
                    if upString not in deadends and upString not in visited:
                        visited.add(upString)
                        fn(upString, turns + 1)
                    if downString not in deadends and downString not in visited:
                        visited.add(downString)
                        fn(downString, turns + 1)
        return fn('0000', 0)

if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0001"
    # deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    # target = "8888"
    sol = Solution()
    print(sol.openLock(deadends, target))
