# Problem available at: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/

'''
Question : 
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return
        
        if len(stones) == 1:
            return stones[-1]
            
        while(len(stones) > 1):

            stones.sort(reverse = True)
            #print('Before processing: ',stones)

            first = stones[0]
            second = stones[1]

            if first == second:
                stones.remove(first)
                stones.remove(second)

            else:
                stones.remove(second)
                stones[stones.index(first)] = first-second

            #print('After processing ',stones)
            
        return stones[0] if stones else 0
