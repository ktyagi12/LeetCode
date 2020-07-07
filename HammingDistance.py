# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/

# Question:
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        output = x^y
        
        output = bin(output)         
        
        return output.count('1')