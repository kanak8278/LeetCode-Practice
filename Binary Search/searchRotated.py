class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(nums, low, high):
            if low > high:
                return -1
            mid = int((low + high) / 2)
            if nums[mid] > target:
                return bSearch(nums, low, mid - 1)
            if nums[mid] < target:
                return bSearch(nums, mid + 1, high)
            if nums[mid] == target:
                return mid

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

        pvt = pivot(0, len(nums) - 1)
        if pvt == -1:
            return bSearch(nums, 0, len(nums) - 1)
        else:
            n1 = nums[:pvt + 1]
            n2 = nums[pvt + 1:]
            s1 = bSearch(n1, 0, len(n1) - 1)
            s2 = bSearch(n2, 0, len(n2) - 1)
            # print(s1, s2)
            result = s2 + 1 + pvt if s2 != -1 else s1
            return result


