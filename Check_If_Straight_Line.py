# Problem: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/


import math

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if not coordinates:
            return 
        
        if len(coordinates) == 2:
            return True
        
        
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
              
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            
            if ((y1-y0)*(x2-x0) != (y2-y0)*(x1-x0)):
                return False
            
        return True