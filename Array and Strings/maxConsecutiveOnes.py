class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = 0
        sum = 0
        for idx, item in enumerate(nums):
            if item == 1 and sum == 0:
                sum += 1
            elif item == 0:
                sum = 0
            elif nums[idx] == 1 and nums[idx - 1] == 1:
                sum += 1

            if sum > max_sum:
                max_sum = sum
        return max_sum