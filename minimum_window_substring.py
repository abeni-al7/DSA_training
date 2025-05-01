class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tCount = Counter(t)
        window = defaultdict(int)

        pointers = [-1, -1]
        minlen = float('inf')
        l = 0
        have, need = 0, len(tCount)
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in tCount and window[char] == tCount[char]:
                have += 1
            
            while have == need:
                if r - l + 1 < minlen:
                    pointers = [l, r]
                    minlen = r - l + 1
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = pointers
        return s[l:r+1] if minlen != float('inf') else ""
        
        
