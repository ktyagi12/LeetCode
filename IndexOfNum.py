#Problem available at: https://leetcode.com/problems/search-insert-position/submissions/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 
        elif(target not in nums):
            j = 0
            nums.sort()
            if target > nums[-1]:
                nums.append(target)
                return nums.index(target)

            elif target < nums[0]:
                nums.insert(0, target)
                return nums.index(target)

            else:       
                while(nums[j] < target):             
                    j = j + 1
                nums.insert(j, target)
                return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return nums.index(target)