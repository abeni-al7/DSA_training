# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i, word in enumerate(strs):
            anagrams[str(sorted(word))].append(i)
        
        output = []
        for key, value in anagrams.items():
            output.append([strs[i] for i in value])
        return output