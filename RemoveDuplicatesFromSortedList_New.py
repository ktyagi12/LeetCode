# Problem available at: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

# Question: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        
        slow = 0
        fast = slow + 1
        
        while(fast < len(nums)):
            
            if nums[slow] == nums[fast]:
                nums[slow] = '$'
            
            slow = fast
            fast += 1
               
        
        while('$' in nums):
            nums.remove('$')
            
                
        return len(nums)