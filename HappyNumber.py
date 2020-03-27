#Problem available at: https://leetcode.com/problems/happy-number/submissions/
class Solution:
    def isHappy(self, n: int) -> bool:
        
        if not n:
            return
        
        hashSet=set()
        hashSet.add(n)
        
        while n!=1:
            
            s=str(n)
            sum=0
            
            for i in range(len(s)):
                sum+=int(s[i])*int(s[i])
            
            if sum in hashSet:
                return False
            else:
                hashSet.add(sum)
            n=sum
        return True
            