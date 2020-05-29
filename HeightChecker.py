# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

# Question:
'''
Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        out_ = heights.copy()
        out_.sort()
        
        count = 0
        
        for i in range(len(heights)):
            if out_[i] != heights[i]:
                count += 1
        
        
        
        return(count)