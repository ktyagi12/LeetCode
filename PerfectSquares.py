# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3373/

# Question: Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        
        if n < 3:
            return n
        
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            
            for num in square_nums:
                
                if(i < num): break
                
                dp[i] = min(dp[i], dp[i-num] + 1)    # +1 is for that square we are substracting.
        
        return dp[-1]