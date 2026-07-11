class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        componentFreq = defaultdict(int)

        for i in range(n):
            graph[i].append(i)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            graph[i].sort()
            componentFreq[tuple(graph[i])] += 1
        
        completeCount = 0
        for k, v in componentFreq.items():
            if len(k) == v:
                completeCount += 1
        return completeCount