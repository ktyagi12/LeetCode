#Problem available at: https://leetcode.com/problems/rotate-array/submissions/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return 
        
        for i in range(k):
            popped_ = nums.pop(-1)
            nums.insert(0,popped_)
            
        return nums