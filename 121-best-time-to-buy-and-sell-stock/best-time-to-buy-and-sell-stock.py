class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in prices[1:]:
            if minimum > i:
                minimum = i
            cal_profit = i - minimum
            profit = max(profit, cal_profit)
        return profit
