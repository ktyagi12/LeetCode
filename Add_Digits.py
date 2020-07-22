# Problem available at: https://leetcode.com/problems/add-digits/submissions/

# Question: Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution:
    def addDigits(self, num: int) -> int:
        
        if not num:
            return 0
        
        while num > 9:
            rem = num %10
            ans = num // 10
            
            num = rem + ans
            
        return num
            
            