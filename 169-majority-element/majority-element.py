class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=res=0
        hashmap={}
        for i in nums:
            hashmap[i] = 1+ hashmap.get(i,0)
            if hashmap[i] > maj:
                res = i
                maj = hashmap[i]
        return res
        

        