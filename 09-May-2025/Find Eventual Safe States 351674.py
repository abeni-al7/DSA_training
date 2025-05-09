# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reversed_graph = [[] for _ in range(len(graph))]
        incoming = [0] * len(graph)
        for node in range(len(graph)):
            for child in graph[node]:
                reversed_graph[child].append(node)
            incoming[node] += len(graph[node])
        
        queue = deque()
        safe = []
        for node in range(len(graph)):
            if incoming[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            safe.append(node)
            for child in reversed_graph[node]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        return sorted(safe)