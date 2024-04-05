class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        minimum = float('inf')
        for i in range(len(strs)):
            minimum = min(len(strs[i]), minimum)
        for i in range(minimum):
            char = ""
            comp = False
            for j in range(len(strs)):
                if len(char) == 0:
                    char += strs[j][i]
                if char[0] != strs[j][i]:
                    char = ""
                    comp = True
                    break
            if comp == True:
                break
            prefix += char
        return prefix
