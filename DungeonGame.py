# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3367/



# Question:
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

'''


class Solution:
     def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        memo = [[[None] * 2 for _ in range(n)] for _ in range(m)] 
        
        def check(health, i, j):
			# compare the knight's health with the memorized dp
            if memo[i][j][0] and health >= memo[i][j][0]:
                return True
            if memo[i][j][1] and health <= memo[i][j][1]:
                return False
            if health <= 0:
                return False
              
            res = None
            
            if i == m-1 and j == n-1:
                res =  health + dungeon[i][j] > 0
            
            elif i == m-1:
                res = check(health + dungeon[i][j], i, j+1)
            
            elif j == n-1:
                res = check(health + dungeon[i][j], i+1, j)
            
            else:
                res = check(health + dungeon[i][j], i+1, j) or check(health + dungeon[i][j], i, j+1)
            
			# if the knight can rescue the princess, memorize his health at memo[i][j][0], otherwise memo[i][j][1]
            if res: 
                memo[i][j][0] = health
                return True
            else:
                memo[i][j][1] = health
                return False
                
		# binary search
        low, high = 0, 2**31
        while low < high:
            mid = low + (high-low)//2
            if check(mid, 0, 0):
                high = mid
            else:
                low = mid + 1

        return low
        
