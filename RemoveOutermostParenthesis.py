#Problem available at: https://leetcode.com/problems/remove-outermost-parentheses/submissions/
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return
        
        dict_ = {'(':')', ')':'('}
        stack = []
        
        str_ = ''
        
        start = 0
        end = 0
          
        for i in range(len(S)):
            if stack and dict_[S[i]] == stack[-1]:
                stack.pop()
                
                if not stack: 
                    end = i
                    str_ = str_ + S[start+1 : end]
                    start = i+1
                    
                
            else:
                stack.append(S[i])
                
        return str_