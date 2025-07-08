# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        i = 0
        while i < len(points) - 1:
            if points[i + 1][0] <= points[i][1] <= points[i + 1][1]:
                points[i + 1][1] = points[i][1]
                points.pop(i)
            else:
                i += 1

        return len(points)
