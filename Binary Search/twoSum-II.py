class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, n in enumerate(numbers):
            if idx == len(numbers) - 1:
                return
            idxx = self.bSearch(numbers[idx + 1:], 0, len(numbers[idx + 1:]) - 1, target - n)
            if idxx != -1:
                return idx + 1, idxx + idx + 2

    def bSearch(self, nums, low, high, target):
        pivot = int((low + high) / 2)
        print(pivot, low, high)
        if low > high:
            return -1
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            return self.bSearch(nums, low, pivot - 1, target)
        elif nums[pivot] < target:
            return self.bSearch(nums, pivot + 1, high, target)
        else:
            return -1
