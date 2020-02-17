#Problem available at: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
from collections import Counter

class Solution:
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return list(set(range(1, len(nums)+1)) - set(nums))
        