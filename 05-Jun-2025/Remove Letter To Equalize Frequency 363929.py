# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            # Remove character at index i
            temp = word[:i] + word[i+1:]
            freq = Counter(temp)
            # Get frequency values and check if all are the same
            values = list(freq.values())
            if len(set(values)) == 1:
                return True
        return False