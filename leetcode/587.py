class Solution:
    def outerTrees(self, trees: list) -> list:
        res = []
        x_min, x_max, y_min, y_max = trees[0][0], trees[0][0], trees[0][1], trees[0][1]
        for x, y in trees:
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y

        

        return res