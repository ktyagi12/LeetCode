# Problem available at: https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/

# Question: Write a function that takes a string as input and reverse only the vowels of a string.

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        if not s:
            return ''
        
        vowels = set("AaEeIiOoUu")
        
        data = list(s)
        
        i, j = 0, len(data) - 1
        
        while i < j:
            
            if data[i] in vowels and data[j] in vowels:
            
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1
                
            if data[i] not in vowels:
                i += 1
                
            if data[j] not in vowels:  
                j -= 1
                
        return "".join(data)
    