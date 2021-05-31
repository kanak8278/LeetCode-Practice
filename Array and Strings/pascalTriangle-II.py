class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = []
        for idx in range(rowIndex + 1):
            l = []
            for i in range(idx + 1):
                l.append(None)
            memo.append(l)

        # print(memo)
        # return
        def utility(rowIndex, columnIndex):
            if rowIndex == columnIndex or columnIndex == 0:
                memo[rowIndex][columnIndex] = 1
                return memo[rowIndex][columnIndex]
            else:
                if memo[rowIndex][columnIndex] is None:
                    memo[rowIndex][columnIndex] = utility(rowIndex - 1, columnIndex) + utility(rowIndex - 1,
                                                                                               columnIndex - 1)
                return memo[rowIndex][columnIndex]

        for x in range(rowIndex + 1):
            utility(rowIndex, x)

        return (memo[rowIndex])
