# PROBLEM: SINGLE NUMBER: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

# Logic: The key which will have the value 1, will be the single number.

from collections import Counter
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        if not nums:								# when input is not given.
            return
        
        counter = Counter(nums)						# Generating a dictionary of input list nums
        
        for key in counter.keys():					# Iterating over the keys of dictionary.
            if counter[key] == 1:
                return key
            else:
                pass