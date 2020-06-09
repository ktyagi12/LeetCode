# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

# Question: Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if not n:
            return False
        
        if n <= 0:
            return False
        
        while(n != 1):
            
            if n%2!= 0:
                return False
            
            n = n//2
        return True