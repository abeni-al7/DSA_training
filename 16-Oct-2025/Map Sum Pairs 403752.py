# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        num = val
        if key in self.visited:
            num -= self.visited[key]
        curr = self.root
        for char in key:
            i = ord(char) - ord("a")
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.value += num
        self.visited[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            i = ord(char) - ord("a")
            if not curr.children[i]:
                return 0
            curr = curr.children[i]
        return curr.value



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)