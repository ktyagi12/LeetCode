# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3360/

# Question:
'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        from collections import defaultdict
        d = defaultdict(list)
        
        for u, v, w in flights:
            d[u].append((w,v))
        
        from heapq import heappop, heappush
        h = [(0, -1, src)] # cost, k, node
        weights = {} 
        
        while h:
            cost, k, node = heappop(h)
            
            if cost > weights.get((k, node), float('inf')) or k > K:
                continue 
            if node == dst:
                return cost
            
            for edgeCost, nei in d[node]:
                newCost = edgeCost + cost
                
                if weights.get((k+1, nei), float('inf')) > newCost:
                    
                    weights[(k+1, nei)] = newCost
                    heappush(h, (newCost, k+1, nei))
        return -1 
