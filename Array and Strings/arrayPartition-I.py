class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mx_sum = 0
        for idx in range(0, len(nums), 2):
            mx_sum += min(nums[idx], nums[idx + 1])
        return mx_sum

