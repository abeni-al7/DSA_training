# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, accounts):
        self.parent = {}
        self.size = defaultdict(int)
        for account in accounts:
            for i in range(1, len(account)):
                self.parent[(account[0], account[i])] = (account[0], account[i])
                self.size[(account[0], account[i])] = 1
    
    def get(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.get(self.parent[node])
        return self.parent[node]
    
    def union(self, nodeX, nodeY):
        parX, parY = self.get(nodeX), self.get(nodeY)
        if parX == parY:
            return
        if self.size[parX] >= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]
    
    def get_merged(self):
        ans = defaultdict(list)
        for k in self.parent:
            v = self.get(k)
            ans[v].append(k[1])
        return ans
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        
        for account in accounts:
            par = (account[0], account[1])
            for i in range(1, len(account)):
                uf.union(par, (account[0], account[i]))
        
        merged = uf.get_merged()
        print(merged)
        res = []
        for k in merged:
            curr = []
            for val in merged[k]:
                curr.append(val)
            curr.sort()
            res.append([k[0]] + curr)
        
        return res
        
