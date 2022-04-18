class Solution:
    def shortestToChar(self, s: str, c: str) -> list:
        res = [10 ** 6] * len(s)

        for i in range(len(s)):
            if s[i] == c:
                res[i] = 0

                j = i - 1
                while j >= 0:
                    if res[j] > res[j + 1] + 1:
                        res[j] = res[j + 1] + 1
                        j = j - 1
                    else:
                        break
            else:
                if i != 0:
                    res[i] = res[i - 1] + 1

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.shortestToChar("aaab", "b")
    print(res)
