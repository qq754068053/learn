from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list) -> list:
        res = []
        m, n = len(heights), len(heights[0])

        # 找到所有可以流入上方和左方的小岛屿
        pacific = set()
        q = deque()

        for i in range(n):
            q.append([0, i])
            pacific.add((0, i))
        for i in range(1, m):
            q.append([i, 0])
            pacific.add((i, 0))

        while len(q) != 0:
            x, y = q.popleft()
            for ax, ay in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + ax, y + ay
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in pacific:
                    q.append([nx, ny])
                    pacific.add((nx, ny))

        return res
