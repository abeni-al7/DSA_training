class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for c, pre in prerequisites:
            graph[pre].append(c)
            indegree[c] += 1
        
        queue = deque([])
        visited = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)
        
        while queue:
            current = queue.popleft()
            for nei in graph[current]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    visited.add(nei)
        print(visited, len(visited))

        return len(visited) == numCourses

            
