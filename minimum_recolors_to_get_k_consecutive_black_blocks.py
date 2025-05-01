class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[:k])
        minOps = count['W']
        l = 0
        for r in range(k, len(blocks)):
            count[blocks[r]] += 1
            count[blocks[l]] -= 1
            l += 1
            minOps = min(minOps, count['W'])
        return minOps
        
