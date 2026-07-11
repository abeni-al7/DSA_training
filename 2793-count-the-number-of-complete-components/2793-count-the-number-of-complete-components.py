class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        completeCount = 0
        visited = set()

        def dfs(curr, info):
            visited.add(curr)
            info[0] += 1
            info[1] += len(graph[curr])

            for child in graph[curr]:
                if child not in visited:
                    dfs(child, info)
            
        for i in range(n):
            if i in visited:
                continue
            
            componentInfo = [0, 0]
            dfs(i, componentInfo)

            if componentInfo[0] * (componentInfo[0] - 1) == componentInfo[1]:
                completeCount += 1
        return completeCount