#Problem available at: https://leetcode.com/problems/power-of-three/submissions/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        
        if not n:
            return False
        if n == 1:
            return True
        
        sum_ = 3
        while(1):
            
            if sum_ < n:
                sum_ *= 3
                
            elif sum_ == n:
                return True
            
            else:
                return False
            
        