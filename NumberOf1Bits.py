#Problem available at: https://leetcode.com/problems/number-of-1-bits/submissions/
from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        if not n:
            return 0
        
        counter = Counter(str(bin(n)))
        
        if counter.__contains__('1'):
            return  counter['1'] 
        else:
            return 0
        