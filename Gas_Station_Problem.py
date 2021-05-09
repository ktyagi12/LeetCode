# Problem: https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_ind = 0
        surplus = deficit = 0
        
        for i in range(len(gas)):
            surplus = surplus + gas[i] - cost[i]
            
            if surplus < 0:
                deficit += surplus
                surplus = 0
                start_ind = i+1
                
        if (surplus + deficit) >= 0:
            return start_ind
        else:
            return -1            