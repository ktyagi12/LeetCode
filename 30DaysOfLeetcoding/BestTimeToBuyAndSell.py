# Problem available at : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

# Question: 
'''
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        
        for i in range(len(prices)-1):
            j = i+1
            
            curr_profit = prices[j] - prices[i]
            if (curr_profit) > 0:
                profit += curr_profit
                
            
        return profit
        