#Problem available at: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        if not mat or not k:
            return
        
        
        soldier_list = []
        k_weak = []
        
        for row in range(len(mat)):
            sum_ = 0
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    sum_ += 1
            soldier_list.append(sum_)
            
        #print(soldier_list)
        
        for i,j in enumerate(soldier_list):
            k_weak.append((i,j))
        k_weak.sort(key = lambda k_weak: k_weak[1])
        
        print(k_weak)
        
        k_lst = []
        for i in range(len(k_weak)):
            if len(k_lst) <k:
                k_lst.append(k_weak[i][0])
            
        return k_lst 