class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def bSearch(low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if low == high:
                if letters[mid] > target:
                    return mid
                else:
                    return -1
            if letters[mid] <= target:
                return bSearch(mid + 1, high)
            else:
                return bSearch(low, mid)

        rs = bSearch(0, len(letters) - 1)
        if rs == -1:
            return letters[0]
        return letters[rs]

