class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        color = [0] * numCourses

        for c, pre in prerequisites:
            graph[pre].append(c)
        
        def can_order(node):
            if color[node] == 1:
                return False

            color[node] = 1
            for c in graph[node]:
                if color[c] == 2:
                    continue
                if not can_order(c):
                    return False

            color[node] = 2
            return True
        
        for i, c in enumerate(color):
            if c == 0:
                if not can_order(i):
                    return False
        return True

            
