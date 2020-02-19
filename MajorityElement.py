#Problem available at: https://leetcode.com/problems/majority-element/submissions/
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        n = len(nums)//2
        majority = nums[0]
        
        for key in counter.keys():
            if counter[key] > n and counter[key] > counter[majority]:
                majority = key
            
        return majority
            