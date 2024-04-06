class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []
        minfreq = [float('inf')] * 26
        for i in range(len(words)):
            charfreq = [0] * 26
            for j in range(len(words[i])):
                charfreq[ord(words[i][j])-ord('a')] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], charfreq[i])
        for i in range(26):
            while minfreq[i] > 0:
                common.append(chr(i + ord('a')))
                minfreq[i] -= 1
        return common
