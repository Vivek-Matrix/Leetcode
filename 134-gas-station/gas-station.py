class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        startPoint=0
        leftfuel=0
        for index in range(0,len(gas)):
            leftfuel+=gas[index]-cost[index]
            if leftfuel<0:
                startPoint=index+1
                leftfuel=0
        return startPoint 