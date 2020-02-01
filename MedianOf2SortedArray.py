#Problem available at: https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in nums2:
            nums1.append(i)
        
        nums1.sort()
        
        if len(nums1)%2 == 0:
            mid1 = len(nums1)//2
            mid2 = ((len(nums1)//2) -1)
            return((nums1[mid1] + nums1[mid2])/2)
            #return (nums1[len(nums1)//2] + nums1[(len(nums1)/2 -1)])/2 
        else:
            return nums1[len(nums1)//2]
        