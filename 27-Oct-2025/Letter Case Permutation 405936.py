# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        valid = set()
        store = {}
        index = 0
        for i, char in enumerate(s):
            if char.isalpha():
                store[index] = i
                index += 1
        
        bitmask = 0
        for i in range(2 ** len(s)):
            curr = ""
            for j in range(len(s)):
                if s[j].isnumeric():
                    curr += s[j]
                elif bitmask & (1 << j):
                    curr += s[j].upper()
                else:
                    curr += s[j].lower()
            valid.add(curr)
            bitmask += 1
        
        return list(valid)
