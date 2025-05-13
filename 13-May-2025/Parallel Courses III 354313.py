# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        for pre, course in relations:
            graph[pre].append(course)
        
        max_time = {}
        def dfs(node):
            if node in max_time:
                return max_time[node]
            
            curr = time[node - 1]
            for course in graph[node]:
                curr = max(curr, time[node - 1] + dfs(course))
            max_time[node] = curr
            return curr

        for i in range(1, n + 1):
            dfs(i)
        return max(max_time.values())