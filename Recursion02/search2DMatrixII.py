class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def fn(low, high):
            h_i, h_j = high
            l_i, l_j = low
            piv_i = int((h_i + l_i) / 2)
            piv_j = int((h_j + l_j) / 2)

            if matrix[piv_i][piv_j] == target:
                print("True", matrix[piv_i][piv_j])
                return True
            if matrix[piv_i][piv_j] > target:
                print("greater", matrix[piv_i][piv_j])
                fn((l_i, l_j), (piv_i, piv_j))
                fn((l_i, piv_j), (piv_i, h_j))
                fn((piv_i, l_i), (h_i, piv_j))
            if matrix[piv_i][piv_j] < target:
                print("smaller", matrix[piv_i][piv_j])
                fn((l_i, piv_j), (piv_i, h_j))
                fn((piv_i, l_i), (h_i, piv_j))
                fn((piv_i, piv_j), (h_i, h_j))
            else:
                return False

        return fn((0, 0), (m, n))