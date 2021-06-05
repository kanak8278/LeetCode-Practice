class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def utility(current, n):
            if current == n:
                return 1
            if current > n:
                return 0
            else:
                if current in memo:
                    return memo[current]

                memo[current] = utility(current + 1, n) + utility(current + 2, n)
                return memo[current]

        return utility(0, n)