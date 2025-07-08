# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        mid = len(costs) // 2
        return sum(a for a, b in costs[:mid]) + sum(b for a, b in costs[mid:])