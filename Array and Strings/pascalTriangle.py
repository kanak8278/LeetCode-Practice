class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            l = [None] * (i + 1)
            arr.append(l)
        # print(arr)

        arr[0][0] = 1
        if numRows == 1:
            return arr
        arr[1][0] = arr[1][1] = 1
        if numRows == 2:
            return arr

        for idx in range(2, len(arr)):
            for idxx in range(len(arr[idx])):
                # print(idx, idxx)
                if idxx == 0 or idx == idxx:
                    arr[idx][idxx] = 1
                    continue
                arr[idx][idxx] = arr[idx - 1][idxx] + arr[idx - 1][idxx - 1]
        return arr



