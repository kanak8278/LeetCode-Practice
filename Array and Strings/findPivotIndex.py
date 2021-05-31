class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = []
        post_sum = []

        for idx, _ in enumerate(nums):
            if idx == 0:
                pre_sum.append(nums[idx])
                continue
            pre_sum.append(nums[idx] + pre_sum[idx - 1])
        rev_nums = nums[::-1]
        for idx, num in enumerate(rev_nums):
            if idx == 0:
                post_sum.append(rev_nums[idx])
            else:
                post_sum.append(rev_nums[idx] + post_sum[idx - 1])

        post_sum = post_sum[::-1]
        for idx in range(len(nums)):
            print(idx)
            if idx == 0:
                if 0 == post_sum[idx + 1]:
                    return idx
            elif idx == len(nums) - 1:
                if 0 == pre_sum[idx - 1]:
                    return idx
            elif pre_sum[idx - 1] == post_sum[idx + 1]:
                return idx
        return -1




