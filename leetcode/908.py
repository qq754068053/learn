class Solution:
    def smallestRangeI(self, nums: list, k: int) -> int:
        iNum, aNum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > aNum:
                aNum = nums[i]
            if nums[i] < iNum:
                iNum = nums[i]

        if aNum - iNum <= k * 2:
            return 0

        return aNum - iNum - k * 2
