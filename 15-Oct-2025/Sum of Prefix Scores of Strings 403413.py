# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.score += 1
        curr.is_end = True
    
    def calculate_score(self, word: str) -> int:
        result = 0
        curr = self.root
        for char in word:
            result += curr.children[char].score
            curr = curr.children[char]
        return result

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []

        for word in words:
            self.insert(word)
        
        for word in words:
            ans.append(self.calculate_score(word))
        return ans
        