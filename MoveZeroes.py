#Problem available at: https://leetcode.com/problems/move-zeroes/submissions/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(nums[i])
            else:
                pass
        return nums
                
        