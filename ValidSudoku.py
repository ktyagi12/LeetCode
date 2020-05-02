# Problem available at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

# Question: 

'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_items = {i: set() for i in range(9)}
        box_items = {i: set() for i in range(9)}

        for i in range(9):
            row_items = set()
            for j in range(9):
                if board[i][j].isdigit():
                    item = board[i][j]
                    if item in row_items or item in column_items[j]:
                        return False
                    row_items.add(item)
                    column_items[j].add(item)

                    index = (i // 3) * 3 + j // 3
                    if item in box_items[index]:
                        return False
                    box_items[index].add(item)

        return True
