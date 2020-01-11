#Problem available at: https://leetcode.com/problems/add-binary/submissions/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_ = 0
        sum_2 = 0
        l1 = len(a)
        l2 = len(b)
        
        for i in range(l1):
            sum_ = sum_ + int(a[i])*(2** (l1-(i+1)))

        for i in range(l2):
            sum_2 = sum_2 + int(b[i])*(2** (l2-(i+1)))
            
        sum_1 = sum_ + sum_2
        s = "{0:b}".format(sum_1)
        return s
            
            
            
            