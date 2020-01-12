#Problem available at: https://leetcode.com/problems/count-and-say/submissions/
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def c_s(s):
        
            ans = []
            counter = 1
            
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    counter = counter + 1
                else:
                    ans.append(str(counter) + s[i])
                    counter = 1
            
            ans.append(str(counter) + s[-1])
            return "".join(ans)
        
        answer = '1'
        for i in range(1,n):
            answer = c_s(answer)
          
        return answer