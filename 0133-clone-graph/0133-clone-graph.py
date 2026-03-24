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

        def dfs(current):
            if current in clone:
                return clone[current]
            
            new = Node(current.val)
            clone[current] = new
            for nei in current.neighbors:
                new.neighbors.append(dfs(nei))
            return new
        
        return dfs(node)

"""
    clone = {1: 1, 2: 2, 4: 4}
    queue = deque([4])
    visited = {1}

    
"""
