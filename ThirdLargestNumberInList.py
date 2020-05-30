# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

# Question: Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = list(set(nums))
        
        if len(nums) <= 2:
            return max(nums)
              
        nums.sort(reverse = True)
        
        return nums[2]