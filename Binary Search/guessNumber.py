# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def fn(low, high):
            if low > high:
                return -1
            mid = int((low + high) / 2)
            print(low, mid, high)
            if guess(mid) == 0:
                return mid
            if guess(mid) == 1:
                return fn(mid + 1, high)
            if guess(mid) == -1:
                return fn(low, mid - 1)

        return fn(1, n)

