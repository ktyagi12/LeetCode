#Problem available at: https://leetcode.com/problems/reverse-bits/submissions/
class Solution:
    def reverseBits(self, n: int) -> int:
       
        bin_n = bin(n)[2:].zfill(32)
         
        return int(bin_n[::-1] ,2)
            