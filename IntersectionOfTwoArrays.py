#Problem available at: https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return
        res = []
        
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
                
        return res
                