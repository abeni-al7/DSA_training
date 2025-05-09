# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        incoming = [0] * n
        for source, dest in edges:
            graph[source].append(dest)
            incoming[dest] += 1
        
        queue = deque()
        answer = [set() for _ in range(n)]
        for node in range(n):
            if incoming[node] == 0:
                queue.append((node, -1))
        
        while queue:
            node, anc = queue.popleft()
            for child in graph[node]:
                if anc != -1:
                    answer[child].update([node, anc])  
                    answer[child].update(answer[node])
                    answer[child].update(answer[anc])      
                else:
                    answer[child].add(node)
                    answer[child].update(answer[node])
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append((child, node))
        
        for i in range(len(answer)):
            answer[i] = sorted(list(answer[i]))
        
        return answer