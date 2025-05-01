class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        k = len(s1)
        if k == 1:
            if s1 in s2:
                return True
            else:
                return False
        curr = Counter(s2[:k])
        l = 0
        for r in range(k, len(s2)):
            if curr == target:
                return True
            curr[s2[l]] -= 1
            l += 1
            if curr[s2[l]] == 0:
                del curr[s1[l]]
            if curr.get(s2[r]):
                curr[s2[r]] += 1
            else:
                curr[s2[r]] = 1
        if curr == target:
            return True
        return False
