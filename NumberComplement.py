# Problem available at: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

# Question: Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        
        if not num:
            return 0
        
        bin_ = bin(num)     
        bin_ = bin_[2:]
        
        out_ = ''
        
        for i in range(len(bin_)):
            if bin_[i] == '1':
                out_ += '0'
                
            else:
                out_ += '1'
                
        out_ = int(out_,2)
        
        return out_