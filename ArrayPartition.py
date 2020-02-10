#Problem available at: https://leetcode.com/problems/array-partition-i/submissions/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        if not nums:
            return
        
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_ += nums[i]
            
        return sum_