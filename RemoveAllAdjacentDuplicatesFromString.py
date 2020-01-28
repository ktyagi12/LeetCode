#Problem available at: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return
        
        stack = [S[0]]
        
        for i in range(1,len(S)):
            if stack and stack[-1] == S[i]:
                stack.pop()
                
            else:
                stack.append(S[i])
            
            
        return "".join(stack)