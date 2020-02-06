#Problem available at: https://leetcode.com/problems/keyboard-row/submissions/
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        if not words:
            return
        
        my_dict = {
            'Q':1,'W':1,'E':1,'R':1,'T':1,'Y':1,'U':1,'I':1,'O':1,'P':1,
            'A':2,'S':2,'D':2,'F':2,'G':2,'H':2,'J':2,'K':2,'L':2,
            'Z':3,'X':3,'C':3,'V':3,'B':3,'N':3,'M':3                
        }
        
        ans = []
        for inp in words:
            var1 = my_dict[inp[0].upper()]
            for char in inp.upper():
                if var1 != my_dict[char]:
                    break
            else:
                ans.append(inp)
        return ans