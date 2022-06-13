class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s) - i):
                if i == 0:
                    dp[j][j] = 1
                else:
                    dp[j][j + i] = dp[j][j + i] + dp[j][j + i - 1] + dp[j + 1][j + i]
                    if s[j] != s[j + i]:
                        dp[j][j + i] = dp[j][j + i] - dp[j + 1][j + i - 1]
        return dp[0][-1]


if __name__ == '__main__':
    s = Solution()
    r = s.countPalindromicSubsequences("bccb")
    print(r)
