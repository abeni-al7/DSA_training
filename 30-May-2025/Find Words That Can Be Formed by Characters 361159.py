# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        result = 0
        word_map = defaultdict(int)
        for word in words:
            for char in word:
                word_map[char] += 1
                if word_map[char] > count[char]:
                    break
            else:
                result += len(word)
            word_map.clear()
        return result