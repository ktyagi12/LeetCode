#Problem available at: https://leetcode.com/problems/unique-email-addresses/submissions/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        if not emails:
            return
        
        set_ = set()
        for email in emails:
            email_l = email.split('@')
            local_name = email_l[0]
            domain_name = email_l[1]
            
            if '.' in local_name:
                local_name = local_name.replace('.','')
            
            if '+' in local_name:
                ind = local_name.index('+')
                local_name = local_name[:ind]
                
            mail=local_name + '@'+ domain_name
            set_.add(mail)
            
        return len(set_)