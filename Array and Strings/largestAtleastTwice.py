import math


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num, idx_max = self.max_num(nums)
        # print(max_num, idx_max)

        for idx, num in enumerate(nums):
            # print(idx)
            if num == max_num:
                continue
            else:
                if max_num < 2 * num:
                    # print(idx, num)
                    return -1
        return idx_max

    def max_num(self, nums):
        max_idx = -1
        max_num = -math.inf
        for i, x in enumerate(nums):
            if x > max_num:
                max_num = x
                max_idx = i
        return max_num, max_idx

