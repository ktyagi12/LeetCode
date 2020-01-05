#Problem available at: https://leetcode.com/problems/roman-to-integer/submissions/

def find_num(ele):
        char_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000,'D':500}
        return char_dict[ele]

class Solution:
    def romanToInt(self,s: str) -> int:
        num = 0
        for i in range(len(s)):
            if ((i+1) < len(s)):
                if(find_num(s[i]) >= find_num(s[i+1])):
                    num = num + find_num(s[i])
                else:
                    num = num - find_num(s[i])
            else:
                num = num + find_num(s[i])
        return(num)