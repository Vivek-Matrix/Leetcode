class Solution:
    def reverse(self, x: int) -> int:
        if x <0:
            res = -int(str(abs(x))[::-1])
        else:
            res = int(str(x)[::-1])
        if res<2**31-1 and res>-2**31:
            return res
        return 0