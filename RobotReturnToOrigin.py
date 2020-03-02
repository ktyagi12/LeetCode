#Problem available at: https://leetcode.com/problems/robot-return-to-origin/submissions/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
         
            if not moves:
                return 
            
            dict_ = {'U': 2, 'D': -2, 'L': -1, 'R': 1}
            sum_moves = 0
            
            for move in moves:
                sum_moves += dict_[move]
                
            return True if sum_moves == 0 else False       


# OR

 return moves.count('U') == moves.count('D') and moves.count("R") == moves.count("L")