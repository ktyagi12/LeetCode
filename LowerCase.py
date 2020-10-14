#Problem available at: https://leetcode.com/problems/to-lower-case/submissions/
class Solution:
    def toLowerCase(self, str: str) -> str:
        
        if not str:
            return
        
        return str.lower()
    
    
    
 OR
 class Solution:
    def toLowerCase(self, str: str) -> str:
        
        if not str:
            return
        
        return str.swapcase()
    
