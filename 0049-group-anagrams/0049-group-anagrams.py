class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1
            key = tuple(key)
            if groups.get(key):
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())