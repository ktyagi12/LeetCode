# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

# Question: 
'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
'''


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sum_left = 0
        sum_right = 0
        
        costs_sorted = sorted(costs, key = lambda x : x[0]- x[1])
        for i in range(len(costs_sorted)//2):
            sum_left += costs_sorted[i][0]
            
        for i in range(len(costs_sorted)//2, len(costs_sorted)):
            sum_right += costs_sorted[i][1]
        
        
            
        return sum_left + sum_right