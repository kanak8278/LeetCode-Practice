class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_nums = []
        for idx, _ in enumerate(nums):
            if idx == 0:
                prefix_nums.append(nums[0])
                continue
            prefix_nums.append(nums[idx] + prefix_nums[idx - 1])
        # print(prefix_nums)

        for idx in range(len(prefix_nums)):
            for i in range(idx, len(prefix_nums)):
                # print(idx, i)
                if i == idx:
                    # print(prefix_nums[i])
                    if prefix_nums[i] >= target:
                        return idx + 1
                else:
                    if (prefix_nums[i] - prefix_nums[i - idx - 1]) >= target:
                        print(prefix_nums[i] - prefix_nums[i - idx - 1], target)
                        return idx + 1

        return 0
