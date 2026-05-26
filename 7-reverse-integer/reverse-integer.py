class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        rev=0
        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        res = sign*int(rev)
        

        mini , maxi = -2**31 , 2**31 - 1
        if res > mini and res < maxi:
            return res
        return 0