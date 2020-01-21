#Problem available at: https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        arr = collections.deque(range(N))
        
        ans = [0]*N
        
        for card in sorted(deck):
            ans[arr.popleft()] = card
            
            if arr:
                arr.append(arr.popleft())
            
        return ans