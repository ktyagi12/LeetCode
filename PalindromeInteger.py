#Problem available at: https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num= x
        rev = 0
        if(x<0):
            return False
        while(num>0):
            rem = num%10
            rev = rev*10 +rem
            num=num//10
        if(rev == x):
            return True
        else:
            return False
        