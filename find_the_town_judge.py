from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in trust:
            graph[a].append(b)
        judge = -1
        for i in range(1, n + 1):
            if len(graph[i]) == 0:
                judge = i
        for i in range(1, n + 1):
            if i == judge:
                continue
            if judge not in graph[i]:
                return -1
        return judge
        