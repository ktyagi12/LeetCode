#Problem available at: https://leetcode.com/problems/reverse-string/submissions/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(0,len(s)//2):
            s[i], s[(n-1) -i] = s[(n-1) -i], s[i]
        
        