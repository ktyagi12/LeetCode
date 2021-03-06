#Problem available at: https://leetcode.com/problems/reverse-string/submissions/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(0,len(s)//2):
            s[i], s[(n-1) -i] = s[(n-1) -i], s[i]
        
        

#=======================================================================================================================================================================

# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        l = 0
        r = len(s) - 1
        
        while(l< r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
