# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        queue = deque()
        order = []
        for node in range(numCourses):
            if incoming[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for child in graph[node]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        if len(order) != numCourses:
            return []
        return order