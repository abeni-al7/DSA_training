class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if groups.get(key):
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())