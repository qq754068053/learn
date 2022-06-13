import math
import random


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        max_num = math.floor(math.sqrt(n)) + 1
        res = 0
        for i in range(1, max_num):
            x = ((n << 1) // i + 1 - i) >> 1
            if ((x << 1) + i - 1) * i == (n << 1):
                res = res + 1

        math.radians()

        return res


if __name__ == '__main__':
    s = Solution()
    r = s.consecutiveNumbersSum(10)
    print(r)
