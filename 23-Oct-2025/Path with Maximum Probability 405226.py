# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            u, v = edge
            w = succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        probs = [0] * n
        probs[start_node] = 1
        heap = [(-1, start_node)]
        visited = set()

        while heap:
            prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            prob = -prob

            for child, weight in graph[node]:
                new_prob = prob * weight
                if new_prob > probs[child]:
                    probs[child] = new_prob
                    heapq.heappush(heap, (-new_prob, child))
        return probs[end_node]
