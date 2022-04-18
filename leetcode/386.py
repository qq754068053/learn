class Solution:
    """
    暂无题解
    """
    def lexicalOrder(self, n: int) -> list:
        res = []

        def dfs(x: int) -> None:
            if x <= n:
                res.append(x)
                for i in range(0, 10):
                    dfs(x * 10 + i)

        for j in range(1, 10):
            dfs(j)

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lexicalOrder(30)
    print(res)
