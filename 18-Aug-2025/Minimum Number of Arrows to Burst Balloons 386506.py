# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0], reverse=True)
        i = 0
        count = 0
        while i < len(points):
            j = i + 1
            while j < len(points) and points[j][0] <= points[i][0] <= points[j][1]:
                j += 1
            count += 1
            i = j
        return count