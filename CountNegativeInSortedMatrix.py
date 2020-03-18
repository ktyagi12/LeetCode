#Problem availabel at: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 
        
        count_ = 0
        
        for list_ in grid:
            for l in list_:
                if l < 0:
                    count_ += 1
                    
        return count_
            
#====================================================================

class Solution:
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def bi(nums, l, r):
            idx = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
                    idx = mid   
            #print(idx)
            return idx
                    
            
        ans = 0
        
        n = len(grid[0])
        right = n-1
        
        for i in range(len(grid)):
            right = len(grid[i])-1
            idx = bi(grid[i],0,right) # index of last non-negative
            
            ans += (n-1-idx) 
            
            #right = idx
        
        return ans
           
