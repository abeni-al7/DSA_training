# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        target = Counter(p)
        current = Counter(s[:k])
        
        anagrams = []
        if current == target:
            anagrams.append(0)
        l = 0
        for r in range(k, len(s)):
            current[s[r]] += 1
            current[s[l]] -= 1
            l += 1
            if current == target:
                anagrams.append(l)
        return anagrams        