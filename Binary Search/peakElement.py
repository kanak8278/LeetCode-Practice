class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return 0

        def fn(low, high):
            print(nums[low], nums[high])
            if nums[low] > nums[low + 1]:
                return low
            if nums[high] > nums[high - 1]:
                return high
            mid = (low + high) // 2
            if mid != high and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return fn(mid + 1, high)
            else:
                return fn(low, mid - 1)

        return (fn(0, len(nums) - 1))

