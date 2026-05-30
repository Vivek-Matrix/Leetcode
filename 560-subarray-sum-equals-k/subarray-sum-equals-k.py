class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c= 0
        p = 0
        d={0:1}
        for i in nums:
            p+=i
            if p-k in d:
                c+=d[p-k]
            d[p] = d.get(p,0)+1
        return c