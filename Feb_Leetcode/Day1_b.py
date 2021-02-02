# Problem statement available at: https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

#Solution 2: Optimised

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        n = bin(n)[2:]
        
        dict_ = Counter(n)
        
        return dict_['1']        

#===========================================================================        