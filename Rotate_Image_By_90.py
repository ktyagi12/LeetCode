# Problem available at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

# Question:
'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        n = len(matrix)
        
        for i in range(n):
            
            for j in range(i):
                
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
                
        for i in range(n):
            
            for j in range(n//2):
                
                matrix[i][j], matrix[i][n - 1 - j] =   matrix[i][n - 1 - j], matrix[i][j]
                
        
                
        