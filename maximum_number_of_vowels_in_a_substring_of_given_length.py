class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        max_ans = 0
        ans = 0
        for r in range(len(s)):
            if r - l + 1 <= k:
                if s[r] in vowels:
                    ans += 1
            else:
                if s[l] in vowels:
                    ans -= 1
                l += 1
                if s[r] in vowels:
                    ans += 1
            max_ans = max(ans, max_ans)
        return max_ans

        
