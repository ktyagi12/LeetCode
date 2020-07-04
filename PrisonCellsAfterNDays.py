# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/

# Question: 
'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

'''

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def nextDay(cells):
            mask = cells.copy()
            for i in range(1, len(cells) - 1):
                if mask[i-1] ^ mask[i+1] == 0:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cells[0] = 0
            cells[-1] = 0   
            return cells
        
        day1 = tuple(nextDay(cells))
        N -= 1
        count = 0
        
        while N > 0:
            day = tuple(nextDay(cells))
            N -= 1
            count += 1
            
            if day == day1:
                N = N % count
        return cells