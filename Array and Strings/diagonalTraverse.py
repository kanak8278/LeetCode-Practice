class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        l = []
        m = len(mat)
        n = len(mat[0])

        def fn(i, j):
            # print(i, j)
            if 0 <= i < m and 0 <= j < n:
                # print("Inside the First Case")
                if (i + j) % 2 == 0:
                    while True:
                        l.append(mat[i][j])
                        if i - 1 >= 0 and j + 1 <= n - 1:
                            i -= 1
                            j += 1
                        else:
                            break
                    if j < n - 1:
                        return fn(i, j + 1)
                    else:
                        return fn(i + 1, j)

                elif (i + j) % 2 == 1:
                    # print("Run Case 2")
                    while True:
                        l.append(mat[i][j])
                        if i + 1 < m and j - 1 >= 0:
                            i += 1
                            j -= 1
                        else:
                            break
                    if i < m - 1:
                        return fn(i + 1, j)
                    else:
                        return fn(i, j + 1)

        fn(0, 0)
        return l

