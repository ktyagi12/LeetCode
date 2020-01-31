#Problem available at: https://leetcode.com/problems/backspace-string-compare/submissions/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        
        stack1 = []
        stack2 = []
        
        for i in S:
            if i != '#':
                stack1.append(i) 
            elif stack1:
                stack1.pop()
            
        for j in T:
            if j != '#':
                stack2.append(j) 
            elif stack2:
                stack2.pop()
                
        return True if stack1 == stack2 else False
            
            
        