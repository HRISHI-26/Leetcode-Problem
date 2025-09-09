class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer approach
        min_price = max(prices)
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
