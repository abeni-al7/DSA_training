# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append((i))
        queue = deque([[headID, 0]])
        time = 0
        while queue:
            node, curr = queue.popleft()
            time = max(time, curr)
            for neighbor in graph[node]:
                queue.append([neighbor, curr + informTime[node]])
        return time