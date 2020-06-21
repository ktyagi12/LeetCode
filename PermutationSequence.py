# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/

# Question :
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        if not n or not k:
            return ''
        
        out_ = ''
        fact = [1]* n
        
        for i in range(1, n):
            fact[i] = i * fact[i-1]
        
        l = [i for i in range (1, n+1)]
        
        k -= 1
      
        for i in range(n-1,-1, -1):
            
            ind = k//fact[i]
            
            out_ = out_ + str(l.pop(ind))
            
            k = k % fact[i]
            
            
        return out_
        
        
        
        
        