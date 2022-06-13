import concurrent.futures


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        length = len(s)

        one_cnt = 0
        for i in range(length):
            if s[i] == "1":
                one_cnt = one_cnt + 1

        res = one_cnt

        current_one = 0
        for i in range(length):
            current = current_one + length - i - one_cnt + current_one
            res = min(res, current)

        return res


if __name__ == '__main__':
    s = Solution()
    r = s.minFlipsMonoIncr("00011000")
    print(r)
