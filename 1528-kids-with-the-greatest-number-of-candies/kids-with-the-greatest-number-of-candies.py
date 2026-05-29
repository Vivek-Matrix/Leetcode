class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=[]
        for i in candies:
            if i+extraCandies < max(candies):
                r.append(False)
            else:
                r.append(True)
        return r