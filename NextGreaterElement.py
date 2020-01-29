#Problem available at: https://leetcode.com/problems/next-greater-element-i/submissions/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return
        
        nums3 = []
        for i in nums1:
            
            if i not in nums2:
                nums3.append(-1)
            
            elif i in nums2 and nums2.index(i) == -1:
                nums3.append(-1)
                
            else:
                for j in range(nums2.index(i)+1, len(nums2)):
                    if i< nums2[j]:
                        nums3.append(nums2[j])
                        break
                        
                else:
                    nums3.append(-1)
                        
        return nums3
 
#=============================================================================================

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return
        
        dict_ = {}    
        stack = []
        
        for i in nums2:
            
            while stack and stack[-1] < i:
                dict_[stack.pop()] = i
            stack.append(i)
        
        return [dict_[x] if x in dict_ else -1 for x in nums1]