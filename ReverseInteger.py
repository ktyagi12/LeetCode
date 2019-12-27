#Problem available at: https://leetcode.com/problems/reverse-integer/submissions/

import sys
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = x
        
        if(x<0):
            num=num*(-1)
        
        while(num>0):
            rem = num%10
            num = num//10
            rev = rev*10 +rem
            
        min_r = -2**31
        max_r = 2**31 -1
            
        if (rev not in range(min_r,max_r)):
            return 0
            
        if(x<0):
            return '-' + str(rev)
        return rev