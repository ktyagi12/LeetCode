#Problem available at: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        dict_ = {'(':')'}
        stack = []
        
        if not S:
            return 0
        
        for s in S:
            print(s)
            if stack and stack[-1] == '(' and dict_[stack[-1]] == s:
                stack.pop()
                
            else:
                stack.append(s)
                
        return len(stack)