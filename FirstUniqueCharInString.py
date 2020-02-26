#Problem available at: https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        list_ = list(s)
        
        dict_ = Counter(s)
        
        for key in dict_.keys():
            if dict_[key] == 1:
                return list_.index(key)
            
        return -1

#================================================

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
                
        dict_ = Counter(s)
        
        for ind,ch in enumerate(s):
            if dict_[ch] == 1:
                return ind
            
        return -1        