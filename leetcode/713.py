class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        res = 0

        i, j = 0, -1
        multi = 1
        while i < len(nums):
            multi = multi * nums[i]
            while multi >= k and j < i:
                j = j + 1
                multi = multi // nums[j]
            res = res + i - j
            i = i + 1

        return res
