# Space: O(n)
# Time: O(n)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        l = []
        m = len(mat)
        n = len(mat[0])

        def fn(i, j):
            if 0 <= i < m and 0 <= j < n:
                mtrx = []
                # mtrx.append(mat[i][j])
                x = i
                y = j
                while x < m and y >= 0:
                    mtrx.append(mat[x][y])
                    x = x + 1
                    y = y - 1
                # print(mtrx)
                if (i + j) % 2 == 1:
                    l.extend(mtrx)
                if (i + j) % 2 == 0:
                    l.extend(mtrx[::-1])
                if j < n - 1:
                    return fn(i, j + 1)
                else:
                    return fn(i + 1, j)

        fn(0, 0)
        return l

