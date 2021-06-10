class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            else:
                mid = int(len(nums) / 2)
                left_list = mergesort(nums[:mid])
                right_list = mergesort(nums[mid:])
                return merge(left_list, right_list)

        def merge(left_list, right_list):
            left = 0
            right = 0
            ret = []
            while left < len(left_list) and right < len(right_list):
                if left_list[left] < right_list[right]:
                    ret.append(left_list[left])
                    left += 1
                else:
                    ret.append(right_list[right])
                    right += 1

            ret.extend(left_list[left:])
            ret.extend(right_list[right:])
            return ret

        return mergesort(nums)
