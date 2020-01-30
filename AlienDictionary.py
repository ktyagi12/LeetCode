#Problem available at: https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return
        
        for i in range(len(words)-1):
            
            first = words[i]
            second = words[i+1]
            
            f1, f2 = len(first), len(second)
            
            j, k = 0, 0
            
            while(first[j] == second[k]):
                j +=1
                k +=1
                if k == f2 or j == f1:
                    break
            if k == f2:
                return False
            
            l1 = order.index(first[j]) 
            l2 = order.index(second[k])
           
            if l1 is not None and l1 is not -1 and l2 is not None and l2 is not -1:
                if l1 > l2:
                    return False
                
        return True