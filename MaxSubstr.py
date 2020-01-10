#Problem available at: https://leetcode.com/problems/maximum-subarray/submissions/
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