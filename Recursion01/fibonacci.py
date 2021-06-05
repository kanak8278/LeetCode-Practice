class Solution:
    def fib(self, n: int) -> int:
        dct = {}

        def utility(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            else:
                if n in dct.keys():
                    return dct[n]
                else:
                    dct[n] = utility(n - 1) + utility(n - 2)
                    return dct[n]

        return utility(n)
