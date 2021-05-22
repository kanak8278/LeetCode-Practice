from typing import List


# class Solution:
#     def twoSum(self, nums, target):
#         for idx, x in enumerate(nums):
#             for idxx, y in enumerate(nums[idx + 1:]):
#                 # print(x, y)
#                 if x + y == target:
#                     return idx, idx + idxx + 1
#
#
# def binarySearch(nums, start, low, high, target):
#     if low <= high:
#         mid = int((low + high) / 2)
#         # print(nums[mid])
#         if start + nums[mid] == target:
#             return mid
#         if start + nums[mid] > target:
#             high = mid - 1
#             return binarySearch(nums, start, low, high, target)
#         if start + nums[mid] < target:
#             low = mid + 1
#             return binarySearch(nums, start, low, high, target)
#     else:
#         return -1
#
#
# if __name__ == "__main__":
#     nums = [-1, 0]
#     target = -1
#     # solution = Solution()
#     # sol = solution.twoSum(nums, target)
#     # print(sol)
#     for idx, x in enumerate(nums):
#         # print("Start: ", x)
#         result = binarySearch(nums, x, 0, len(nums), target)
#         if result != -1:
#             print(idx+1, result+1)
#             break


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, x in enumerate(numbers):
            # print(target)
            if x == target:
                return idx+1, idx+1
            else :
                result = binarySearch(numbers, x, 0, len(numbers), target)
                if result != -1:
                    return idx + 1, result + 1


def binarySearch(nums, start, low, high, target):
    if low <= high:
        mid = int((low + high) / 2)
        # print(nums[mid])
        if start + nums[mid] == target:
            return mid
        if start + nums[mid] > target:
            high = mid - 1
            return binarySearch(nums, start, low, high, target)
        if start + nums[mid] < target:
            low = mid + 1
            return binarySearch(nums, start, low, high, target)
    else:
        return -1


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    sol = solution.twoSum(nums, target)
    print(sol)
