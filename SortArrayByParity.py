#Problem available at: https://leetcode.com/problems/sort-array-by-parity/submissions/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        if not A:
            return
        
        even_list = []
        odd_list = []
        
        for i in A:
            if i%2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
                
        even_list.extend(odd_list)
        return even_list
        