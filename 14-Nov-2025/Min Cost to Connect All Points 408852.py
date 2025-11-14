# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        cost = 0
        visited = set()
        min_heap = [[0, 0]]
        while len(visited) < n:
            c, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            cost += c
            visited.add(i)
            for child_cost, child in adj[i]:
                if child not in visited:
                    heapq.heappush(min_heap, [child_cost, child])
        return cost