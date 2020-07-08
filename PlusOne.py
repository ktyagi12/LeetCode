# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3382/

# Question:
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        merged = int(''.join(str(i) for i in digits))
        
        merged += 1
        
        spl = [int(i) for i in str(merged)]
        
        return spl