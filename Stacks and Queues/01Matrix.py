from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def fn(x, y):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if mat[x][y] == 0:
                return 0
            else:
                q = deque()
                visited = set()
                q.append((x, y))
                visited.add((x, y))
                distance = 0
                while q:
                    distance += 1
                    l = len(q)
                    for _ in range(l):
                        x, y = q.popleft()
                        for dx, dy in dirs:
                            if x + dx in range(len(mat)) and y + dy in range(len(mat[0])) and \
                                    (x + dx, y + dy) not in visited:
                                if mat[x + dx][y + dy] == 0:
                                    return distance
                                else:
                                    q.append((x + dx, y + dy))
                                    visited.add((x + dx, y + dy))

        result = [[None for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for idx1 in range(len(mat)):
            for idx2 in range(len(mat[0])):
                dist = fn(idx1, idx2)
                result[idx1][idx2] = dist

        return result


if __name__ == "__main__":
    # mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    # mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
    sol = Solution()
    print(sol.updateMatrix(mat))
