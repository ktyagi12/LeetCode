#Problem available at: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i]- buy < 0:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit
        