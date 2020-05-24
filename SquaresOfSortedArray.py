#Problem available at: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return
        
        return sorted([i*i for i in A])     
        



# OR =================================================================================================================================================================
# Problem available at:  https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

# Question: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        if not A:
            return 
        
        out_ = []
        for i in range(len(A)):
            sq = A[i] * A[i]
            
            out_.append(sq)    
            
            out_.sort()
            
        return out_