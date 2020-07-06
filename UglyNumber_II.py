# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/

# Question: 
'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        N, m, S = [1], 1, set()
        for _ in range(n):
    		
            while m in S:
                m = heapq.heappop(N)
    		
            S.add(m)
    		
            for i in [2,3,5]: 
                heapq.heappush(N,i*m)
                
        return m