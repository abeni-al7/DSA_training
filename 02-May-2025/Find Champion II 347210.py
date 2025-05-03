# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        weak = set()
        for i in range(n):
            for x in graph[i]:
                weak.add(x)
        champion = -1
        count = 0
        for i in range(n):
            if i not in weak:
                champion = i
                count += 1
        if count != 1:
            return -1
        return champion