class Solution:
    def findMin(self, nums: List[int]) -> int:
        def pivot(low, high):
            if low > high:
                return -1
            mid = int((low + high) / 2)
            print(nums[low], nums[mid], nums[high])
            if mid != len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[low]:
                return pivot(low, mid - 1)
            else:
                return pivot(mid + 1, high)

        point = pivot(0, len(nums) - 1)
        print(point)
        return nums[0] if point == -1 else nums[point + 1]

