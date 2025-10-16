# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.indices = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str, index: int) -> None:
        curr = self.root
        for char in word:
            i = ord(char) - ord("a")
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.indices.append(index)

    def search_prefix(self, word: str) -> List[int]:
        result = []
        curr = self.root
        for char in word:
            i = ord(char) - ord("a")
            if not curr.children[i]:
                return []
            curr = curr.children[i]
        result.extend(curr.indices)
        return result


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()

        for i, word in enumerate(words):
            self.prefix.insert(word, i)
            self.suffix.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        pref_i = self.prefix.search_prefix(pref)
        suff_i = self.suffix.search_prefix(suff[::-1])

        i, j = len(pref_i) - 1, len(suff_i) - 1
        while i >= 0 and j >= 0:
            if pref_i[i] == suff_i[j]:
                return pref_i[i]
            elif pref_i[i] > suff_i[j]:
                i -= 1
            else:
                j -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)