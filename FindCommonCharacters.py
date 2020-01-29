#Problem available at:https://leetcode.com/problems/find-common-characters/submissions/
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        if not A:
            return
        
        result = []
        flag = False
        current_word = A[0]
        min_len = len(current_word)
        
        for i in A:
          
            if len(i) < min_len:
                
                min_len = len(i)
                current_word = i
        
        #print(min_len , current_word)
        A.remove(current_word)
        #print(A)
        
        for j in range(len(current_word)):
            
            curr_char = current_word[j]
            #print('Current character: ',curr_char)
            
            for k in range(len(A)):
                if curr_char in A[k]:
                    flag = True
                    ind = A[k].index(curr_char)
                    A[k] = A[k][0:ind] + A[k][ind+1: ]
                    
                else:
                    flag = False
                    break
            
            if flag == True:
                result.append(curr_char)
                    
        #print('Res: ', result)
        return result
            
            