# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

# Question: Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dict_ = {0: -1}
        count = 0
        max_len = 0
        
        for ind, val in enumerate(nums):
            if val == 0:
                count -= 1
                
            else:
                count += 1
            
            if count not in dict_.keys():
                dict_[count] = ind
                
            else:
                max_len = max(max_len, (ind - dict_[count]))
                
        return max_len