class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def bSearch(low, high):
            if low <= high:
                mid = (low + high) // 2
                print(low, mid, high)
                if mid * mid == num:
                    return True
                if mid * mid < num:
                    return bSearch(mid + 1, high)
                if mid * mid > num:
                    return bSearch(low, mid - 1)

        if num == 1:
            return num
        return bSearch(0, num - 1)
