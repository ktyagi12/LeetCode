# Problem availabel at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

# Question:
'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

'''

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        if not s or not shift:
            return
        
        shifts = 0
        for curr_ in shift:
            if curr_[0] == 0:
                shifts  -= curr_[1]
            elif curr_[0] == 1:
                shifts  += curr_[1]

        for sh in range(abs(shifts)):
            s = list(s)
            if shifts < 0:
                popped = s.pop(0)
                s.append(popped)

            elif shifts > 0:
                popped = s.pop(-1)
                s.insert(0,popped)
            
            elif shifts == 0:
                return ''.join(s)
        return(''.join(s))
            
                    
                    