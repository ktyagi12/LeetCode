#Problem available at: https://leetcode.com/problems/implement-strstr/submissions/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0 
        j = 0
        flag = -1
        size_n = len(needle)
        size_h = len(haystack)
        
        if needle == '':          
            return 0
        elif (len(needle) > len(haystack)):
            return -1
        else:
            while(i< size_h):
                
                if (j < size_n):
                    
                    if(i + (size_n - 1) < size_h):    
                        
                        if (haystack[i] == needle[j] and haystack[i + (size_n - 1)] == needle[-1]):
                            #print('Inside Temp')
                            temp = haystack[i:i + size_n]
                            #print(temp)
                            
                            if (size_n > len(temp)):
                                flag = -1
                                break
                            elif(temp == needle):
                                ind = i
                                flag = 1
                                break
                            else:
                                flag = -1
                                i = i+1
                        else:
                            #print('Inside Else')
                            i = i+1
                    else:
                        flag = -1
                        break
            if flag == -1:
                #print('-1')
                return -1
            else:
                #print(ind)
                return ind