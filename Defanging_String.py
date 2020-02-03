#Problem available at: https://leetcode.com/problems/defanging-an-ip-address/submissions/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        if not str:
            return
        
        address = address.replace('.', '[.]')
        
        return address
        