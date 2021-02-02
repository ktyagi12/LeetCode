# Problem statement available at: https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

#Solution 1: Bruteforce

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
               
        n = bin(n)
        
        n = n[2:]
        
        for i in n:
            if i == '1':
                count += 1
                  
        
        return count
#===========================================================================