class Solution:
    def numberOfMatches(self, n: int) -> int:
        played = 0
        while n>1:
            if n%2==0:
                matches = n//2
                adv = n//2
            else:
                matches = (n-1)//2
                adv = ((n-1)//2) + 1
            n = adv
            played+=matches
        return played