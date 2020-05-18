# Problem available at: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

# Question: Given a positive integer num, write a function which returns True if num is a perfect square else False.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if not num:
            return False
        
        if num == 1:
            return True
        
        left = 1
        right = num
        
        while(left <= right):
            mid = left + (right - left)//2
            if mid*mid == num:
                return True
            
            elif mid*mid < num:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return False