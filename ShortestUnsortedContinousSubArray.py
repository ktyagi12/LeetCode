#Problem available at: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/submissions/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_nums = []
        sorted_nums = sorted(nums)
        
        start = 0
        end = len(nums) - 1
        
        for i in range(start, len(nums)):
            if nums[i] == sorted_nums[i]:
                start += 1

            else:
                break

        for j in range(end, start, -1):
            if nums[j] == sorted_nums[j]:
                end -= 1
            else:
                break
        
        result = (end - start) + 1
        return result