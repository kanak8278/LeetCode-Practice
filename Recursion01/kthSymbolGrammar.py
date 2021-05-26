"""
# Brute Approach
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        l = ['']*(n+1)
        l[0] = '0'
        idx = 0
        def utility(idx, n):
            if idx >= n:
                return
            # print(idx)
            for x in l[idx]:
                if x == '0':
                    l[idx+1] += '01'
                if x == '1':
                    l[idx+1] += '10'
            utility(idx+1, n)
        utility(idx, n)
        return(l[idx-1][k-1])
"""

# Optimized Approach
class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent = self.kthGrammar(n - 1, int(k / 2) + k % 2)
        if parent == 1:
            return 1 if k % 2 == 1 else 0
        if parent == 0:
            return 0 if k % 2 == 1 else 1

