# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        ordered = sorted(costs, key=lambda x: x[1] - x[0])
        total = 0
        for i in range(n // 2):
            total += ordered[i][1]
        for i in range(n // 2, n):
            total += ordered[i][0]
        return total