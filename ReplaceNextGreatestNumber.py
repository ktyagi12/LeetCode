#Problem available at : https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return
        
        max_ = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_
            
            if temp > max_:
                max_ =  temp
        
        return arr