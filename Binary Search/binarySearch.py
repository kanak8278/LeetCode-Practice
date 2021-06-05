class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(low, high):
            if high < low:
                return -1
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bSearch(low, mid - 1)
            elif nums[mid] < target:
                return bSearch(mid + 1, high)

        return (bSearch(0, len(nums) - 1))
