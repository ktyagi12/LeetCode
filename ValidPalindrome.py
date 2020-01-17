#Problem available at: https://leetcode.com/problems/valid-palindrome/submissions/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(c for c in s if c not in string.punctuation).lower().replace(" ","")
                
        return True if s== s[::-1] else False