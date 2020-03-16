#Problem available at: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        if not num:
            return 0
        
        count = 0
        
        while(num >0):
            if num % 2 == 0:
                num /= 2

            elif num % 2 != 0:
                num -= 1
        
            count += 1
        return count