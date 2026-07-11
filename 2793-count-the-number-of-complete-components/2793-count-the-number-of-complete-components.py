class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0
            
        for i in range(n):
            if not visited[i]:
                component = []
                queue = deque([i])
                visited[i] = True

                while queue:
                    current = queue.popleft()
                    component.append(current)

                    for nei in graph[current]:
                        if not visited[nei]:
                            queue.append(nei)
                            visited[nei] = True
                    
                is_complete = True
                for node in component:
                    if len(graph[node]) != len(component) - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components += 1
        return complete_components