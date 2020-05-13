# Problem available at:  https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

# Question: 
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if not ransomNote:
            return True
        
        elif not magazine:
            return False
        
        counter = Counter(magazine)
                
        flag = True
        for i in range(len(ransomNote)):
            
            if counter.__contains__(ransomNote[i]) and counter[ransomNote[i]] > 0:
                    
                counter[ransomNote[i]] -= 1
                
            else:
                flag = False
                
        return flag
