class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        if n == 0:
            return 0
        if n > m:
            return -1
        for idx in range(m - n + 1):
            print(haystack[idx:idx + n])
            if haystack[idx:idx + n] == needle:
                return idx
        return -1
