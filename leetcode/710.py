import random

"""
这是一个不容易理解的方法，其思想是：已知白名单中的元素个数必然有 N-blen 个，我直接生成一个`[0,N-blen)`中的随机数k，
代表我要找白名单中的第k个数；现在我要解决的问题是，如何快速确定**白名单中**的第k个数在**总名单**上的第几个位置。

现假设这个数在**总名单**上的第x个位置（总名单第x个位置的成员就等于x），则有两种情况：

1. 黑名单上所有的数都比x大，那么x左侧不可能含有黑名单成员，直接返回x即可，因为它就是白名单成员之一。
2. 黑名单上有y个数都小于x，那么说明x的左侧一定有y个黑名单成员。所以x实际上是总名单中的第k个数往后再数y个位置的结果，
    其中k等于值x在白名单中的索引。

所以问题就转化成了随机产生一个k，去找到y，从而确定x。

1. 首先对黑名单进行排序
2. 每次调用`pick()`

   1. 先随机产生k
   2. 然后利用二分查找，利用k确定y
      1. 初始low指针=0，high指针=blen-1
      2. 每次`mid=(low+high+1)/2`，
        比较(`B[mid] - mid`与k)【注意⚠️：这里为什么要减去mid呢？其实k表示在白名单的位置，
        mid表示在黑名单的位置，k + mid其实表示在总名单的位置】的大小关系，然后收缩y的范围
   3. 如果y=0，直接返回k；如果y>0，返回k+y+1
"""

class Solution:

    def __init__(self, n: int, blacklist: list):
        """
        :param n: 一个n个数字
        :param blacklist: 有这么多个黑名单数字
        总共有 valid_max = n - len(blacklist) 个有效数字
        所以 rand(0, valid_max)
        对于在黑名单里面的数字, 映射成大于valid_max之后不在黑名单里面的数字
        """
        self.rand_num = dict()
        self.end = n - len(blacklist)

        nums_set = set()
        for black in blacklist:
            if black >= self.end:
                nums_set.add(black)

        start = self.end
        for i in range(len(blacklist)):
            if blacklist[i] < self.end:
                while start in nums_set:
                    start = start + 1
                self.rand_num[blacklist[i]] = start
                start = start + 1

    def pick(self) -> int:
        num = random.randint(0, self.end - 1)
        if num in self.rand_num:
            return self.rand_num[num]
        return num



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()