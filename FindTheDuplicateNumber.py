# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3371/

# Question: 
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for k in counter.keys():
            if counter[k] >1:
                return k
            
        
# =========================================================
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_ = set()
        
        
        for num in nums:
            if num in set_:
                return num
            
            else:
                set_.add(num)