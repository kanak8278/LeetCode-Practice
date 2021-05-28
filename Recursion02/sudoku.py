from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """

        def block(i, j):
            indexes = [(3, 3), (3, 6), (3, 9), (6, 3), (6, 6), (6, 9), (9, 3), (9, 6), (9, 9)]
            for idx, (x, y) in enumerate(indexes):
                if i < x and j < y:
                    return indexes[idx]

        def isPossible(i, j, n):
            (x, y) = block(i, j)
            if n in board[i]:
                return False
            col_board = column_matrix(board)
            if n in col_board[j]:
                return False
            for idx in range(x - 3, x):
                for idxx in range(y - 3, y):
                    if board[idx][idxx] == n:
                        return False
            return True

        def column_matrix(matrix):
            col_matrix = []
            for i in range(9):
                col_matrix.append([row[i] for row in matrix])
            return col_matrix

        def recursion(board, i, j):
            if i >= 9 or j >= 9:
                print(board)
                return
            elif board[i][j] == ".":
                for n in range(1, 10):
                    # print(i, j, n)
                    if isPossible(i, j, str(n)):
                        board[i][j] = str(n)
                        if j == 8:
                            recursion(board, i + 1, 0)
                        else:
                            recursion(board, i, j + 1)
                    board[i][j] = "."
            else:
                if j == 8:
                    recursion(board, i + 1, 0)
                else:
                    recursion(board, i, j + 1)

        recursion(board, 0, 0)
        return
        # print(res_board)


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol = Solution()
    res_board = sol.solveSudoku(board)
    # print(res_board)
