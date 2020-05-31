#Problem available at: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = 1
        if len(nums) == 0:
            return 0
        else:
            while(j<len(nums)):
                if (nums[i] != nums[j]):
                    i = i+1
                    j = j+1
                else:
                    nums.remove(nums[j])
                    
            return len(nums)