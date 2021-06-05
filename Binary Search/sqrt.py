class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        def fn(low, high):
            if low > high:
                return low - 1
            mid = int((low + high) / 2)
            if mid * mid == x or (mid * mid < x and (mid + 1) * (mid + 1) > x):
                return mid
            elif mid * mid < x:
                return fn(mid + 1, high)
            else:
                return fn(low, mid - 1)

        return (fn(0, x - 1))
