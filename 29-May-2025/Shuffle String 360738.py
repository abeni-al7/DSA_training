# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [0] * len(indices)
        for i, char in enumerate(s):
            output[indices[i]] = char
        return "".join(output)