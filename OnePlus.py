#Problem available at: https://leetcode.com/problems/plus-one/submissions/

class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ''
        for i in digits:
            s = s+ str(i)
        
        digit = str(int(s) + 1)
        d = [ int(j) for j in digit]
        return d if digits else 0
