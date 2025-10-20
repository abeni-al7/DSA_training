# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        def dijkstra(graph, start):
            distances = {node: float("inf") for node in range(1, n + 1)}
            distances[start] = 0

            queue = [start]
            while queue:
                node = heapq.heappop(queue)
                for child, weight in graph[node]:
                    distance = distances[node] + weight
                    if distance < distances[child]:
                        distances[child] = distance
                        heapq.heappush(queue, child)
            return distances
        
        duration = dijkstra(graph, k)
        ans = max(duration.values())
        return ans if ans != float("inf") else -1

        