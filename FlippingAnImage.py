#Problem available at:https://leetcode.com/problems/flipping-an-image/submissions/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        if not A:
            return
        
        for row in A:
            for j in range(len(row)//2):
                row[j], row[len(row)- (j+1)] = row[len(row)- (j+1)] ,row[j] 
                
        print('Reverse A',A)       
        
        for row in A:
            for col in range(len(row)):
                if row[col] == 0:
                    row[col] = 1
                else:
                    row[col] = 0
        print('Inverse: ',A)           
        return A