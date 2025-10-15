# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
 
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
    
    def search_prefix(self, word: str) -> str:
        ans = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                return ""
            if char in curr.children:
                curr = curr.children[char]
                ans.append(char)
            if curr.is_end:
                return "".join(ans)
            
        return "".join(ans)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        words = sentence.split(" ")
        for i, word in enumerate(words):
            root = self.search_prefix(word)
            if root:
                words[i] = root

        return " ".join(words)

