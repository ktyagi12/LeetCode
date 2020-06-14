# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/

# Question:
'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        nums.sort()
        dic = collections.defaultdict(list)
        dp = [[num] for num in nums]
        maxLen = 1
        idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j]+[nums[i]]
                    if len(dp[i])>maxLen:
                        maxLen = len(dp[i])
                        idx = i
        return dp[idx]