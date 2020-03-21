#Problem available at: https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if not n:
            return 0
        

        # Initialize the result with 0.
        count = 0

        # Trailing zeroes will exist if number divisible by 10 (5, 2). So the number of 5s in factorisation of number will give the trailing zeroes.
        i = 5
        
        while(n/i >= 1):
            count += n//i
            i *= 5
    
        return count