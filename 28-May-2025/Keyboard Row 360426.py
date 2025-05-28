# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Map each character to its keyboard row number
        row_map = {}
        for ch in "qwertyuiop":
            row_map[ch] = 1
        for ch in "asdfghjkl":
            row_map[ch] = 2
        for ch in "zxcvbnm":
            row_map[ch] = 3
        
        result = []
        for word in words:
            lower_word = word.lower()
            first_row = row_map[lower_word[0]]
            if all(row_map[ch] == first_row for ch in lower_word):
                result.append(word)
        return result