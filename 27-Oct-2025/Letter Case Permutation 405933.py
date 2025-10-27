# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        valid = set()
        def backtrack(i, curr):
            if i >= len(s):
                return
            if s[i].isnumeric():
                backtrack(i + 1, curr)
            perm = curr[:i] + curr[i].lower() + curr[i+1:]
            perm2 = curr[:i] + curr[i].upper() + curr[i+1:]
            valid.add(perm)
            valid.add(perm2)
            backtrack(i + 1, perm)
            backtrack(i + 1, perm2)
        backtrack(0, s)
        return list(valid)
            