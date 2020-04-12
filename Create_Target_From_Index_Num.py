#Problem available at: https://leetcode.com/problems/create-target-array-in-the-given-order/submissions/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        if not nums or not index:
            return
        
        target = []				# Creating target array
        
        i = 0
        
        while(i < len(index)):			
            target.insert(index[i], nums[i])			
                
            #print(nums[i], index[i], target[0:i+1])
            i += 1
            
        return target