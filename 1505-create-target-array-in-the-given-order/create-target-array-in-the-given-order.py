class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        r=[]
        [r.insert(index[i],nums[i]) for i in range(len(nums))]
        return r