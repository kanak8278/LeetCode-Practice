class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def bSearch(nums, low, high, target):
            if low > high:
                return False
            mid = (low + high) // 2
            if nums[mid] == target:
                nums.pop(mid)
                return True
            if nums[mid] < target:
                return bSearch(nums, mid + 1, high, target)
            else:
                return bSearch(nums, low, mid - 1, target)

        intersection_list = []
        nums2.sort()
        for n in nums1:
            print(n)
            # if n in intersection_list:
            #     continue
            search = bSearch(nums2, 0, len(nums2) - 1, n)
            print(search)
            if search:
                intersection_list.append(n)
        return intersection_list
