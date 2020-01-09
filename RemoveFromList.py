#Problem available at: https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        #print('Initially length : ', length)
        i = 0
        while(i < len(nums)):
            if nums[i] == val:
                nums.pop(i)
                length = length - 1
                i = i - 1
                
            i = i + 1
        print(length)