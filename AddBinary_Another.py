#Problem available at: https://leetcode.com/problems/add-binary/submissions/      
                        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = (int(a,2)) + int(b,2)
        return (bin(s)[2:])                   