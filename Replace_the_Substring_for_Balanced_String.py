class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        target = len(s) / 4
        if max(count[i] for i in count) <= target:
            return 0
        minLength = len(s)
        l = 0
        for r in range(len(s)):
            count[s[r]] -= 1
            while max(count[i] for i in count) <= target:
                minLength = min(minLength, r - l + 1)
                count[s[l]] += 1
                l += 1
        return minLength
            

        
        
