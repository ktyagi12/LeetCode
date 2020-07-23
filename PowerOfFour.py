# Problem available at: https://leetcode.com/problems/power-of-four/submissions/

# Question: Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if not num:
            return False
        
        if num < 0:
            return False
        
        while(num % 4 ==0):
            num = num/4
        
        if num == 1:
            return True
        
        return False
