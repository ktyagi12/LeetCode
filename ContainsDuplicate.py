#Problem available at: https://leetcode.com/problems/contains-duplicate/submissions/
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter.keys():
            if counter[i] >1:
                return True

        return False