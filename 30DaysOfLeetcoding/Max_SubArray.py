# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/

# Question: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return nums[0]
        if all(i < 0  for i in nums):
            return max(nums)

        sum_ele = 0
        max_till = 0
        for i in nums:
            sum_ele = sum_ele + i

            if(sum_ele < 0):
                sum_ele = 0
            elif(sum_ele > max_till):
                max_till = sum_ele
        return max_till