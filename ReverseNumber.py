# Problem available at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

# Question: Given a 32-bit signed integer, reverse digits of an integer.
'''
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321
'''
class Solution:
    def reverse(self, x: int) -> int:
        
        if not x:
            return 0
        
        res = 0
        flag = 0

        if x < 0:
            x = abs(x)
            flag = 1

        while(x > 0):
            rem = x%10
            x = x // 10
            
            res = res*10 + rem
            
            if res > 2147483647 or res < -2147483648:
        	    return 0


        if flag == 0:
            return res

        else:
            return -res