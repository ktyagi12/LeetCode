# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3384/

# Question: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        prev = float('inf')
        
        for idx, val in enumerate(nums):
        
            if val == prev:
                continue
            
            self.twoSum( nums[idx+1:], -val, ans )
            prev = val
        
        return ans
    
    def twoSum(self, nums, target, ans):
        
        cache = {}
        
        for idx, val in enumerate(nums):
            
            if target - val in cache:
                
                ans.add( (val, target - val, -target) ) # 3 sum wants the numbers, while 2sum wanted the indices
            
            cache[val] = idx   