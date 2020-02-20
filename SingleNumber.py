#Problem available at: https://leetcode.com/problems/single-number/submissions/
from collections import Counter
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        if not nums:
            return
        
        counter = Counter(nums)
        
        for key in counter.keys():
            if counter[key] == 1:
                return key
            else:
                pass
            
        
        