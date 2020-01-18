#Problem available at: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        L = []
        odd_num = 0
        for i in range(n):
            L.append([0]*m)
        
        for j in indices:
            r = j[0]
            c = j[1]
            for e in range(len(L[r])):
                L[r][e] = L[r][e] + 1

            for k in range(n):
                L[k][c] = L[k][c] + 1

        for i in range(n):
            for j in range(m):
                if L[i][j] %2 != 0:
                    odd_num = odd_num +1
                    
        return odd_num


#=============================================================================

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        L= [[0]*m for i in range(n)]
                
        for j in indices:
            r = j[0]
            c = j[1]
            for e in range(m):
                L[r][e] = L[r][e] + 1

            for k in range(n):
                L[k][c] = L[k][c] + 1

        
        return sum(1 for i in L for j in i if j % 2)