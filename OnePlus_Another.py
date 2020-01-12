#Problem available at: https://leetcode.com/problems/plus-one/submissions/
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1,-1):
            if (digits[i] + carry) < 10:
                digits[i] = digits[i] + 1
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1

        if carry ==1:
                digits.insert(0,1)        
        return(digits)