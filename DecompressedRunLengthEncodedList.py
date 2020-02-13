#Problem statement available at: https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        if len(nums) in range(2,101):
            if len(nums)%2 == 0:
                l2 = []
                for i in range(0,len(nums), 2):
                    l1 = []
                    j = i+1
                    while(nums[i]>0):
                        l1.append(nums[j])

                        nums[i] = nums[i] - 1

                    l2.extend(l1)
                return l2
            else:
                return None
        else:
            return None


 #============================================================================

 class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        l2 = []
        for i in range(0,len(nums), 2):
            j = i+1
            while(nums[i]>0):
                l2.append(nums[j])
                nums[i] = nums[i] - 1
        return l2

#============================================================================

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        l2 = []
        for i in range(0,len(nums), 2):
            j = i+1
            cur=[nums[j]]*nums[i]
            l2.extend(cur)
        return l2

#==========================================================================

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        l2 = []
        for i in range(0,len(nums), 2):
            j = i+1
            l2.extend([nums[j]]*nums[i])
            
        return l2