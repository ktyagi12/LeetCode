#Problem available at: https://leetcode.com/problems/climbing-stairs/submissions/
'''
def fib(num):
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)
'''        

class Solution:
    def climbStairs(self, n: int) -> int:
        #return fib(n+1)
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a+b
            
        return a
        