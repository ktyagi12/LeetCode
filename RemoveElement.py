# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

# Question available at:
'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0;
        for j in range(len(nums)):
            if (nums[j] != val):
                
                nums[i] = nums[j]
                i += 1
        
        return i
        