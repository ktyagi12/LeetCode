#Problem available at: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return
        
        return sorted([i*i for i in A])     
        