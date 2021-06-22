from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque()
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q.append((sr, sc))
        color = image[sr][sc]
        image[sr][sc] = newColor
        visited.add((sr, sc))
        while q:
            l = len(q)
            for _ in range(l):
                x, y = q.pop()
                for dx, dy in dirs:
                    if x + dx in range(len(image)) and y + dy in range(len(image[0])) \
                            and image[x + dx][y + dy] == color and (x+dx, y+dy) not in visited:
                        q.append((x + dx, y + dy))
                        image[x + dx][y + dy] = newColor
                        visited.add((x+dx, y+dy))
        return image


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 1, 1]]
    sr, sc = 1, 1
    newColor = 1
    sol = Solution()
    print(sol.floodFill(image, sr, sc, newColor))
