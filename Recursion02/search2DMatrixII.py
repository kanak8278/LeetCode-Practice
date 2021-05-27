class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def fn(row, col):
            if row == m or col == -1:
                return False
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
                return fn(row, col)
            if matrix[row][col] < target:
                row += 1
                return fn(row, col)

        return fn(0, n - 1)
