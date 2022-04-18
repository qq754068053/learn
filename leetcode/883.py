class Solution:
    def projectionArea(self, grid: list) -> int:
        n = len(grid)

        res = 0

        row = grid[0][0]

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    res = res + 1

                if i == 0:
                    if grid[i][j] > row:
                        row = grid[i][j]
                else:
                    grid[i][0] = max(grid[i][0], grid[i][j])
                    grid[0][j] = max(grid[0][j], grid[i][j])

        res = res + grid[0][0] + row

        for i in range(1, n):
            res = res + grid[0][i] + grid[i][0]

        return res
