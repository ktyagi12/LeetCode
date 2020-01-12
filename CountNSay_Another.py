#Problem available at: https://leetcode.com/problems/count-and-say/submissions/
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            prev = '11'
            for i in range(3, n+1):
                ans = ''
                cnt = 1
                prev = prev + '$'
                for j in range(0,len(prev)-1):
                    if prev[j] == prev[j+1]:
                        cnt = cnt + 1
                    else:
                        ans = ans + str(cnt)
                        ans = ans + prev[j]
                        cnt = 1
                prev = ans
            return prev