class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        count = 0
        while (True):
            if nums[idx] == 0:
                nums.pop(idx)
                count += 1
            else:
                idx += 1
            if idx >= len(nums):
                break
        for i in range(count):
            nums.append(0)
        return nums
