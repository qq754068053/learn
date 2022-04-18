class Solution:
    def maxRotateFunction(self, nums: list) -> int:
        total = 0
        temp = 0
        for i in range(len(nums)):
            total = total + nums[i]
            temp = temp + i * nums[i]

        res = temp
        for i in range(1, len(nums)):
            temp = temp + len(nums) * nums[i - 1] - total
            res = max(res, temp)

        return res
