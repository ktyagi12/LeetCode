# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3365/

# Question:
'''
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
'''


class Solution:
    
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h,t,d = 1,0,256

        dic = defaultdict(list)
        for i in range(M-1):  h = (h * d) % q 

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            dic[t].append(i+1)

        for key in dic:
            for i,j in combinations(dic[key], 2):
                if text[i:i+M] == text[j:j+M]:
                    return (True, text[i:i+M])      

        return (False, "")

    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid
        return Found
