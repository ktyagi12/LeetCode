#Problem available at: https://leetcode.com/problems/unique-morse-code-words/submissions/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        if not words:
            return 0
        
        dict_ = { 'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 
'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.','q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-',  'y' : '-.--', 'z' : '--..' }
        
        set_ = set()
        
        for word in words:
            temp = []
            for char in word:
                temp.append(dict_[char])
            
            set_.add(''.join(temp))
        return(len(set_))
        