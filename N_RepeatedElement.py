#Problem available at: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        if not A:
            return
        
        dict_ = {}
        
        for i in A:
            if dict_.__contains__(i):
                dict_[i] = dict_[i] + 1
            else:
                dict_[i] = 1
                
        print(dict_)
        
        return max(dict_, key = dict_.get)
#==============================================================

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        if not A:
            return
        
        dict_ = {}
        
        for i in A:
            if dict_.__contains__(i):
                dict_[i] = dict_[i] + 1
            else:
                dict_[i] = 1
                
        v = list(dict_.values())
        k = list(dict_.keys())
        return k[v.index(max(v))]
#=============================================================

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        if not A:
            return
        
        count = collections.Counter(A)
        print(count)
        for k in count:
            if count[k] > 1:
                return k