# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = defaultdict(int)
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        
        start = 0
        end = 0
        partitions = []
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions