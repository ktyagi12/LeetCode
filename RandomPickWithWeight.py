# Problem available at:  https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/


class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        ranint = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, ranint, 0, len(self.w))
        


# Your Solution object will be instantiated and called as such:

#obj = Solution(w)
#param_1 = obj.pickIndex()