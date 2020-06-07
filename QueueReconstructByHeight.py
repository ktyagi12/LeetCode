# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

# Question:
'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people = sorted(people, key = lambda x: (-x[0], x[1]))

        res = []
        for p in people:
            res.insert(p[1], p)
        return res