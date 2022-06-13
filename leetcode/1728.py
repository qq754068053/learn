import math
from typing import List
import sys


class Solution:

    def __init__(self):
        # 网格信息
        self.grid = []
        # 网格的行和列
        self.row, self.col = 0, 0
        # 喵咪和老鼠每次移动的最大距离
        self.catJump, self.mouseJump = 0, 0
        # 喵咪、老鼠和食物的坐标
        self.catPoint, self.mousePoint, self.foodPoint = [0, 0], [0, 0], [0, 0]
        # 记录喵咪和老鼠的相对位置
        self.pointStatus = set()
        # 老鼠的移动次数
        self.moveCount = 0
        # 老鼠的最大移动次数
        self.MaxMove = 1000

    def init(self, grid: List[str], catJump: int, mouseJump: int):
        self.row, self.col = len(grid), len(grid[0])
        self.catJump, self.mouseJump = catJump, mouseJump
        self.pointStatus = set()
        self.moveCount = 0

        self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == "M":
                    self.mousePoint = [i, j]
                elif grid[i][j] == "C":
                    self.catPoint = [i, j]
                elif grid[i][j] == "F":
                    self.foodPoint = [i, j]
                elif grid[i][j] == "#":
                    self.grid[i][j] = 1

    def isEqualPoint(self, point1: List[int], point2: List[int]) -> bool:
        isEqual = point1[0] == point2[0] and point1[1] == point2[1]
        return isEqual

    def depthFirstSearch(self, mousePoint: List[int], catPoint: List[int], whoMove: int) -> bool:
        # 首先根据whoMove找到需要移动的对象, 默认是喵咪移动, 如果是老鼠移动则需要将移动次数加一
        point, jump = catPoint, self.catJump
        if whoMove == 0:
            point, jump = mousePoint, self.mouseJump
            self.moveCount = self.moveCount + 1

        result = False

        # 找到移动的对象, 需要根据jump找出所有可能到达的位置
        # 首先这里的step表示对象一次移动的步数, 范围取值为[0, jump]
        nextPoint = set()
        for step in range(jump + 1):
            # a表示对象在x轴上移动的距离
            for a in range(step + 1):
                b = step - a    # 根据step和a计算对象在y轴上移动的距离
                for xx, yy in [[a, b], [-a, b], [a, -b], [-a, -b]]:
                    # 这里找到了下一个位置的坐标
                    x, y = point[0] + xx, point[1] + yy
                    # 判断当前坐标在本次dfs中是否已经遍历
                    if (x, y) in nextPoint:
                        continue
                    nextPoint.add((x, y))
                    # 判断是否在网格内或者是否为墙
                    if xx < 0 or xx >= self.row or yy < 0 or yy >= self.col or self.grid[xx][yy] == 1:
                        continue
                    # 喵咪移动
                    #   1、坐标在老鼠上
                    #   2、坐标早食物上
                    if whoMove == 1:
                        if self.isEqualPoint(mousePoint, [xx, yy]) or self.isEqualPoint(self.foodPoint, [xx, yy]):
                            return True
                        status = (xx, yy, mousePoint[0], mousePoint[1], 1)
                        # 当前状态已经访问过
                        if status in self.pointStatus:
                            continue
                        self.pointStatus.add(status)
                        result = result or not self.depthFirstSearch(mousePoint, [xx, yy], 0)
                    # 老鼠移动
                    #   1、坐标在食物上
                    else:
                        if self.isEqualPoint([xx, yy], self.foodPoint):
                            return True
                        status = (xx, yy, catPoint[0], catPoint[1], 0)
                        if status in self.pointStatus:
                            continue
                        self.pointStatus.add(status)
                        if self.moveCount >= self.MaxMove:
                            continue
                        result = result or not self.depthFirstSearch([xx, yy], catPoint, 0)

        # 最后需要将1移动次数减一, 因为这是dfs, 不减一的话会影响其他路径
        self.moveCount = self.moveCount - 1
        return result

    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        self.init(grid, catJump, mouseJump)
        result = self.depthFirstSearch(self.mousePoint, self.catPoint, 0)
        return result


if __name__ == '__main__':
    r = math.ceil(3.0000000000000001)
    print(r)
