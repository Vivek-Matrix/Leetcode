from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i, v in enumerate(s):
            if d[v] == 1:
                return i
        return -1