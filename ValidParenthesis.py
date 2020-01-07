#Problem available at: https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    
    def isValid(self, s: str) -> bool:
        val_dict = {'{': '}','(': ')','[':']','}':'{',']':'[',')':'('}
        val_list = []
        for i in range(len(s)):
            if(len(val_list) == 0):
                val_list.append(s[i])
                #print('Initial push: ', val_list)
            else:
                if (val_dict[s[i]] == val_list[-1]):
                    val_list.pop(-1)
                    #print('After pop: ', val_list)
                else:
                    val_list.append(s[i])
                    #print('Inter push: ', val_list)
                    
        if (len(val_list) == 0):
            return True
        else:
            return False