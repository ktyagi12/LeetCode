# Problem available at:  https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3374/

# Question: 
'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
            stack = []
            res = []
            stack.append("JFK")

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0: 
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())

        return res[::-1]