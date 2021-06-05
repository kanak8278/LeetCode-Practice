class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bSearch(low, high):
            if low > high:
                return [-1, -1]

            mid = (low + high) // 2
            if nums[mid] == target:
                l = mid
                h = mid
                while True:
                    if l - 1 >= 0 and nums[l - 1] == target:
                        l = l - 1
                    else:
                        break
                while True:
                    if h + 1 < len(nums) and nums[h + 1] == target:
                        h = h + 1
                    else:
                        break
                return l, h
            if nums[mid] < target:
                return bSearch(mid + 1, high)
            if nums[mid] > target:
                return bSearch(low, mid - 1)

        return bSearch(0, len(nums) - 1)