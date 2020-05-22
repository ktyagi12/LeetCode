# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

# Question: Given an array nums of integers, return how many of them contain an even number of digits. 

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        even_count = 0
        for i in range(len(nums)):
            count = 0
            while(nums[i] > 0):
                
                nums[i] = nums[i] // 10
                count += 1          
            if count % 2 == 0:
                even_count += 1
                
        return even_count
            