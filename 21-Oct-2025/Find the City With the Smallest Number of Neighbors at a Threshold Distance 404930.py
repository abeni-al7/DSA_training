# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(src):
            heap = [(0, src)]
            valid = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in valid:
                    continue
                valid.add(node)

                for child, weight in graph[node]:
                    if dist + weight <= distanceThreshold:
                        heapq.heappush(heap, (dist + weight, child))
            return len(valid) - 1

        min_len = float("inf")
        ans = -1
        for i in range(n):
            if dijkstra(i) <= min_len:
                min_len = dijkstra(i)
                ans = i
        return ans