#Problem available at: https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time_sec = 0
        p = 0
        q = 1
        while(q< len(points)):
            print(points[p], points[q])
            p_i = points[p][0]
            p_j = points[p][1]

            q_i = points[q][0]
            q_j = points[q][1]

            time_sec = time_sec + max(abs(q_i - p_i), abs(q_j - p_j))

            p = p +1
            q = q +1

        return time_sec
