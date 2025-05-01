from collections import defaultdict
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        hashmap = defaultdict(list)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in hashmap.get(i, []):
                    hashmap[i].append(words[i][j])
        for i in range(len(words)):
            hashmap[i].sort()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if hashmap.get(i) == hashmap.get(j):
                    count += 1
        return count
