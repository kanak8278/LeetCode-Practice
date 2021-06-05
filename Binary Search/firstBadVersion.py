# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if low == high and isBadVersion(mid):
                return low
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        # print(mid)


