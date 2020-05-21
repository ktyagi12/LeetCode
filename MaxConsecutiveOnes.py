# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

# Question: Given a binary array, find the maximum number of consecutive 1s in this array.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        max_ = 0
        curr_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
                if max_ < curr_count:
                    max_ = curr_count
            else:
                curr_count = 0
                if max_ < curr_count:
                    max_ = curr_count
                    
        return max_