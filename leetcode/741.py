import copy
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        aha = copy.deepcopy(grid)
        for i in range(len(aha)):
            for j in range(len(aha)):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    aha[i][j] = aha[i][j] + aha[i][j - 1] if aha[i][j] != -1 and aha[i][j - 1] != -1 else -1
                elif j == 0:
                    aha[i][j] = aha[i][j] + aha[i - 1][j] if aha[i][j] != -1 and aha[i - 1][j] != -1 else -1
                else:
                    aha[i][j] = -1 if aha[i][j] == -1 or (aha[i - 1][j] == -1 and aha[i][j - 1] == -1) else max(
                        aha[i - 1][j], aha[i][j - 1]) + aha[i][j]

        if aha[-1][-1] == -1:
            return 0

        i, j = len(grid) - 1, len(grid) - 1
        while i >= 0 or j >= 0:
            if i == 0 and j == 0:
                break
            if j > 0 and (aha[i][j] == aha[i][j - 1] or (aha[i][j] == aha[i][j - 1] + 1 and grid[i][j] == 1)):
                grid[i][j] = 0
                j = j - 1
            else:
                grid[i][j] = 0
                i = i - 1

        grid[0][0] = 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid) - 1:
                    continue
                elif i == len(grid) - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1] if grid[i][j] != -1 and grid[i][j + 1] != -1 else -1
                elif j == len(grid) - 1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j] if grid[i][j] != -1 and grid[i + 1][j] != -1 else -1
                else:
                    grid[i][j] = -1 if grid[i][j] == -1 or (grid[i + 1][j] == -1 and grid[i][j + 1] == -1) else max(grid[i + 1][j], grid[i][j + 1]) + grid[i][j]

        return aha[-1][-1] + grid[0][0]


if __name__ == '__main__':
    s = Solution()
    s.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]])
