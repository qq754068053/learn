from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums = heights.copy()
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] != heights[i]:
                count = count + 1
        return count


if __name__ == '__main__':
    s = Solution()
    s.heightChecker([1, 3, 2, 5, 4])
