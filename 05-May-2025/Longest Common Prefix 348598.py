# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        common = ""
        end = False
        for i in range(len(first)):
            for string in strs:
                if i >= len(string) or first[i] != string[i]:
                    end = True
                    break
            if end:
                break
            common += first[i]
        return common
                


        