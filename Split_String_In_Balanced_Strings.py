#Problem available at:https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return
        
        r_count = 0
        l_count = 0
        ans = 0
        
        for i in s:
            print('Curr i: ', i)
            if i == 'R':
                r_count = r_count + 1
                
            else:
                l_count = l_count + 1
                
            if r_count == l_count:
                ans += 1
                r_count = 0
                l_count = 0
                
        return ans