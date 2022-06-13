from typing import List
from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.is_match(word, pattern):
                res.append(word)
        return word

    def is_match(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        hashMap = dict()
        char = set()
        for i in range(len(s1)):
            if s1[i] in hashMap:
                if s2[i] != hashMap[s1[i]]:
                    return False
            else:
                if s2[i] in char:
                    return False
                hashMap[s1[i]] = s2[i]
                char.add(s2[i])

        return True


if __name__ == '__main__':
    s = Solution()
