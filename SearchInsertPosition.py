# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/

# Question:
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return 0
        
        if target in nums:
            return nums.index(target)
        
        else:
            
            if target < nums[0]:
                return 0
                
            elif target > nums[-1]:
                return len(nums)
            
            i = 0
            while(target > nums[i]):
                i += 1
            return i    