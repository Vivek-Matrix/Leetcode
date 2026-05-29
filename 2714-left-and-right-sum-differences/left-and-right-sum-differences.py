class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        returner = []
        leftSum = 0
        rightSum = sum(nums)
        for i in nums:
            rightSum -= i
            returner.append(abs(leftSum-rightSum))
            leftSum += i
        return returner