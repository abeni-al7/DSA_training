"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {}

        queue = deque([node])
        visited = set()

        while queue:
            curr = queue.popleft()
            visited.add(curr)

            if curr not in clone:
                new = Node(curr.val)
                clone[curr] = new
            else:
                new = clone[curr]

            for nei in curr.neighbors:
                new_nei = Node(nei.val) if nei not in clone else clone[nei]
                if nei not in clone:
                    new_nei = Node(nei.val)
                    clone[nei] = new_nei
                else:
                    new_nei = clone[nei]

                if new_nei not in new.neighbors:
                    new.neighbors.append(new_nei)
                if nei not in visited:
                    queue.append(nei)
        
        return clone[node]

"""
    clone = {1: 1, 2: 2, 4: 4}
    queue = deque([4])
    visited = {1}

    
"""
