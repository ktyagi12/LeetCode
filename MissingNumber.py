#Problem available at: https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        if not nums:
            return
        
        sum_ = (len(nums) * (len(nums) + 1) / 2)
        
        return  int(sum_ - sum(nums))
            