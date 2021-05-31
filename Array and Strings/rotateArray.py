class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            if start <= end:
                x = nums[start]
                nums[start] = nums[end]
                nums[end] = x
                reverse(nums, start + 1, end - 1)
            else:
                return

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, k, len(nums) - 1)
        reverse(nums, 0, k - 1)




