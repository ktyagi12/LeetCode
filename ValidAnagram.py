#Problem available at: https://leetcode.com/problems/valid-anagram/submissions/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l1 = list(s)
        l1.sort()
        
        l2 = list(t)
        l2.sort()
        
        return True if l1 == l2 else False
        