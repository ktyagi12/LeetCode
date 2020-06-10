# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/


# Question:
'''
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0
        count = 0
        
        while (i< len(s) and j < len(t)):
            if s[i] == t[j]:
                count += 1
                i += 1
                
            j += 1
            
        return True if count == len(s) else False
            
                
            