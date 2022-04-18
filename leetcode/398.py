from random import randint
from collections import defaultdict


class Solution:

    def __init__(self, nums: list):
        self.num2indexes = defaultdict(list)

        for i in range(len(nums)):
            self.num2indexes[nums[i]].append(i)

    def pick(self, target: int) -> int:
        idx = randint(0, len(self.num2indexes[target]) - 1)
        return self.num2indexes[target][idx]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)