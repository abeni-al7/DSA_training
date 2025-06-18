# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = Counter(s1)
        count = Counter(s2[:k])
        if count == target:
            return True
        l = 0
        for r in range(k, len(s2)):
            count[s2[r]] += 1
            count[s2[l]] -= 1
            l += 1
            if count == target:
                return True
        return False
