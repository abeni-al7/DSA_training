# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.parent = {chr(i): chr(i) for i in range(ord("a"), ord("z") + 1)}
    
    def find(self, char):
        if char != self.parent[char]:
            self.parent[char] = self.find(self.parent[char])
        return self.parent[char]
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX == parY:
            return

        if ord(parX) < ord(parY):
            self.parent[parY] = parX
        else:
            self.parent[parX] = parY

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        
        ans = ""
        for i in range(len(baseStr)):
            char = uf.find(baseStr[i])
            ans += char
        return ans