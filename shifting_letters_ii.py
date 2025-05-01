class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = []
        prefix = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            num = 1 if direction == 1 else -1
            prefix[start] += num
            if end + 1 < len(s):
                prefix[end + 1] -= num
        for i in range(1, len(s)):
            prefix[i] += prefix[i-1]
        for i in range(len(s)):
            res.append(chr((ord(s[i]) - ord('a') + (prefix[i] % 26)) % 26 + ord('a')))
        return ''.join(res)

        
