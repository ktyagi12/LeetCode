#Problem available at: https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
class Solution:
    def reverseWords(self, s: str) -> str:
        
        if not s:
            return s
        if s == '':
            return s
        #print('Original s', s)
        
        words = s.split(' ')
        #print('Next words: ', words)
        
        for i in range(len(words)):
            temp = words[i][::-1]
            words[i] = temp
            
        #print(words)
        
        return(' '.join(words))
            