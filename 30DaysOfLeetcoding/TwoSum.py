# Problem available at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

# Question: 
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

# Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return None
            
        counter = dict()
        for i,v in enumerate(nums):
            counter[v] = i
            
        print(counter)

        for k in range(len(nums)):
            
            s1 = nums[k]
            diff = target - s1
            
            if diff in counter.keys():
                sec_ind = counter[diff]
                
                if sec_ind != k:
                    return sorted([sec_ind, k])
            else:
                counter.update({nums[k]:k})
        
# Test Case:
'''
nums : [0,3,4,0]
target : 0
'''