# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in redEdges:
            graph[a].append((b, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))

        queue = deque([(0, -1)])
        visited = set((0, -1))
        locked = [False for _ in range(n)]
        answer = [-1 for _ in range(n)]
        answer[0] = 0
        distance = 0

        while queue:
            for i in range(len(queue)):
                node, curr = queue.popleft()
                if not locked[node]: answer[node] = distance
                locked[node] = True
                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor[1] != curr:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return answer