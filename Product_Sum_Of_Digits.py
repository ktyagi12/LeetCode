#Problem available at: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        if not n:
            return 0
        
        prod_ = 1
        
        sum_ = 0
        
        while(n > 0):
            rem = n % 10
            
            prod_ *= rem
            sum_ += rem
            print(prod_, sum_)
            n = n//10
            
        return (prod_ - sum_)