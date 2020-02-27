#Problem available at: https://leetcode.com/problems/excel-sheet-column-number/submissions/

class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return
        
        num = 0
        for c in s:
            num = num * 26 + ord(c) - ord('A') + 1
        return num
  