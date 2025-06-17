# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if k > n:
            return []
        
        target = Counter(p)
        window = Counter(s[:k])

        matches = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if target[c] == window[c]:
                matches += 1
        
        res = []
        if matches == 26:
            res.append(0)
        
        l = 0
        for r in range(k, n):
            c1 = s[l]
            if window[c1] == target[c1]:
                matches -= 1
            window[c1] -= 1
            if window[c1] == target[c1]:
                matches += 1
            
            c2 = s[r]
            if window[c2] == target[c2]:
                matches -= 1
            window[c2] += 1
            if window[c2] == target[c2]:
                matches += 1

            if matches == 26:
                res.append(l + 1)

            l += 1
            
        return res