# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = [[] for _ in range(n + 1)]
        queue = deque([1])
        res = -1
        curr = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == n:
                    if res != -1:
                        return curr
                    res = curr
                for child in graph[node]:
                    if len(visit[child]) == 0 or (len(visit[child]) == 1 and visit[child][0] != curr):
                        visit[child].append(curr)
                        queue.append(child)
            if (curr // change) % 2:
                curr += change - (curr % change) 
            curr += time
