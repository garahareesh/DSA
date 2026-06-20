class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        profit = 0
        max_profit =0
        for price in prices:
            min_value=min(min_value, price)
            profit = price-min_value
            max_profit = max(max_profit,profit)
        return max_profit

        