# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        curr = self.root
        for char in word:
            i = ord(char) - ord("a")
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            i = ord(char) - ord("a")
            curr = curr.children[i]
        return curr.is_end

    def longestWord(self, words: List[str]) -> str:
        words.sort()
        max_len = 0
        ans = ""

        for word in words:
            self.insert(word)
        
        for word in words:
            length = 0
            for i in range(len(word)):
                if not self.search(word[:i+1]):
                    length = 0
                    break
                length += 1
            if length > max_len:
                max_len = length
                ans = word
        return ans
        