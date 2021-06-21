from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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

        string = '0000'
        if string in deadends:
            return -1
        if string == target:
            return 0
        if target in deadends:
            return -1
        q = deque()
        visited = set()
        q.append(string)
        visited.add(string)
        turns = 0
        while q:
            turns += 1
            for x in range(len(q)):
                string = q.popleft()
                for idx in range(4):
                    upString = moveUp(string, idx)
                    downString = moveDown(string, idx)
                    if upString == target or downString == target:
                        return turns
                    if upString not in deadends and upString not in visited:
                        q.append(upString)
                        visited.add(upString)
                    if downString not in deadends and downString not in visited:
                        q.append(downString)
                        visited.add(downString)

        return -1


if __name__ == "__main__":
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # target = "0202"
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "0009"
    sol = Solution()
    print(sol.openLock(deadends, target))
