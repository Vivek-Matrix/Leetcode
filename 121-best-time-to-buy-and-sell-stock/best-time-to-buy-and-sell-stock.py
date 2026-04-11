class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        min_price = float('inf')
        profit = 0
        for price in prices:
            min_price = min(min_price,price)
            profit = max(profit, price - min_price)
        return profit


        