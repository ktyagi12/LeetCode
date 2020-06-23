# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3368/

# Question: Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if not nums:
            return 
        
        counter = Counter(nums)
        #print(counter)
        
        for k in counter.keys():
            if counter[k] == 1:
                return k