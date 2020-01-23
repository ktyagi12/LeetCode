#Problem available at: https://leetcode.com/problems/baseball-game/submissions/
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        sum_ = 0
        stack = []
        
        for i in ops:
            if i == 'C':
                sum_ = sum_ - int(stack.pop())
                  
            elif i == 'D':
                doubled = int(stack[-1]) * 2
                stack.append(str(doubled))
                sum_ = sum_ + doubled
                
                
            elif i == '+':
                
                added = int(stack[-1]) + int(stack[-2])
                stack.append(added)
                sum_ = sum_ + added
            
            else:
            
                stack.append(i)
                sum_ = sum_ + int(i)
                
                
        return sum_