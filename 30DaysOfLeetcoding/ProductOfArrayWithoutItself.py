# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

# Question:
'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
'''



import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return
        
        result = [0]* len(nums)
        left = [0]* len(nums)
        right = [0]* len(nums)
        
        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        right[len(nums)-1] = 1
        for j in range(len(nums)-2, -1,-1):
            right[j] = right[j+1] * nums[j+1]
        
        
        for k in range(len(nums)):
            result[k] = left[k] * right[k]
            
            
        return result
    