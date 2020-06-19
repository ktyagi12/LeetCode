# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3364/

# Question: 
'''
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        list_ = []

        for idx, val in enumerate(sorted(citations, reverse = True)):

            list_.append(min(idx+1, val))

        return (max(list_))
