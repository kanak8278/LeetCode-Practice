class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        while (True):
            if len(nums) <= idx or idx >= len(nums) - 1:
                break
            if nums[idx] == nums[idx + 1]:
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)
