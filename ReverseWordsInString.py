# Problem available at:https://leetcode.com/problems/reverse-words-in-a-string/

# Question: Given an input string, reverse the string word by word.

class Solution:
    def reverseWords(self, s: str) -> str:
        
        if not s:
            return ''
        
        return (' '.join(s.split()[::-1]))
