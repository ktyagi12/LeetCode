#Problem available at: https://leetcode.com/problems/jewels-and-stones/submissions/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        if not J or not S:
            return
        
        dict_ = {}
        
        for s in S:
            if dict_.__contains__(s):
                dict_[s] = dict_[s] +1 
            else:
                dict_[s] = 1
        
        
        print(dict_)
        sum_ = 0
        for i in J:
            if dict_.__contains__(i):
                sum_ = sum_ + dict_[i]
                print('i: ', i , 'sum: ', sum_)
                
        return sum_
            
        