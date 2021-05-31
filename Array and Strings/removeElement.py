class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while (True):
            if idx >= len(nums):
                break
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)


