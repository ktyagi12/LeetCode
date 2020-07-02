# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

# Question:
'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if not n:
            return 0
        
        
        count = 1
        while n >= count:
            n -= count
            count += 1
        
        return count-1