# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

# Question:

'''
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        if not arr:
            return
        
        sum_ = 0
        
        for i in range(len(arr)):
            if (arr[i] + 1) in arr:
                sum_ += 1
            else:
                pass
        return sum_