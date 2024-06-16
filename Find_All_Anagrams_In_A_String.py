class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        target = Counter(p)
        curr = Counter(s[:k])
        l = 0
        answer = []
        for r in range(k, len(s)):
            if curr == target:
                answer.append(l)
            curr[s[l]] -= 1
            if curr[s[l]] == 0:
                del curr[s[l]]
            l += 1
            if curr.get(s[r]):
                curr[s[r]] += 1
            else:
                curr[s[r]] = 1
        if curr == target:
            answer.append(l)
        return answer
