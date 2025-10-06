# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 2)

        for i in range(len(cost) - 2, -1, -1):
            memo[i] = min(cost[i] + memo[i+1], cost[i+1] + memo[i+2])
        
        return memo[0]