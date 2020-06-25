# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3370/

# Question: Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

class Solution:
    
    def numTrees(self, n: int) -> int:
        
        if not n:
            return 0
        
        table = [0]*(n+1)
        table[0] = 1
        
        for i in range(1, n+1):
            
            for j in range(i):
                
                table[i] += table[j] * table[i-1-j]
        
        return table[-1]
        