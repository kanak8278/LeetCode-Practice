# One issue in code, Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 6 get printed twice

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        pointers = [[0, 0], [0, m - 1], [n - 1, m - 1], [n - 1, 0]]
        lst = []
        while True:
            print(pointers)
            print(pointers[1][1] - pointers[0][1] + 1)
            for i in range(pointers[1][1] - pointers[0][1] + 1):
                lst.append(matrix[pointers[0][0]][pointers[0][1] + i])
            print(pointers[2][0] - pointers[1][0] + 1)
            for i in range(1, pointers[2][0] - pointers[1][0] + 1):
                lst.append(matrix[pointers[1][0] + i][pointers[1][1]])
            print(pointers[2][1] - pointers[3][1] + 1)
            for i in range(1, pointers[2][1] - pointers[3][1] + 1):
                lst.append(matrix[pointers[3][0]][pointers[2][1] - i])
            print(pointers[3][0] - pointers[0][0])
            for i in range(1, pointers[3][0] - pointers[0][0]):
                lst.append(matrix[pointers[3][0] - i][pointers[3][1]])
            if pointers[1][1] - pointers[1][0] <= 1 or pointers[3][0] - pointers[0][0] <= 1:
                return lst[:n * m]
                break
            else:
                pointers[0][0] = pointers[0][0] + 1
                pointers[0][1] = pointers[0][1] + 1
                pointers[1][0] = pointers[1][0] + 1
                pointers[1][1] = pointers[1][1] - 1
                pointers[2][0] = pointers[2][0] - 1
                pointers[2][1] = pointers[2][1] - 1
                pointers[3][0] = pointers[3][0] - 1
                pointers[3][1] = pointers[3][1] + 1


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]

    sol = Solution()
    print(sol.spiralOrder(matrix))

    # print(lst)
