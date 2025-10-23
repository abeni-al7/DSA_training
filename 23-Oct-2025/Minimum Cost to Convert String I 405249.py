# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(original)):
            graph[original[i]].append((changed[i], cost[i]))
        
        memo = {}
        def dijkstra(s, t):
            if (s, t) in memo:
                return memo[(s, t)]
            costs = {}
            costs[s] = 0
            heap = [(0, s)]

            while heap:
                c, node = heapq.heappop(heap)
                
                for child, cur in graph[node]:
                    if child in costs and c + cur >= costs[child]:
                        continue
                    costs[child] = c + cur
                    heapq.heappush(heap, (c + cur, child))

            for k, v in costs.items():
                memo[(s, k)] = v
            return memo[(s, t)] if (s, t) in memo else -1
        
        total = 0
        for i in range(len(source)):
            curr = dijkstra(source[i], target[i])
            if curr == -1:
                return -1
            total += curr
        return total
            