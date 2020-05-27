# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

# Question: Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if not arr:
            return False
        
        counter = Counter(arr)
        
        for num in arr:
            if num*2 == num and counter[num] >=2:
                return True
            
            if num*2 != num and num*2 in counter:
                return True
            
        return False
            