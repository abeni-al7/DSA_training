# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False
        
        target = [0] * 26
        window = [0] * 26

        for char in s1:
            idx = ord(char) - ord("a")
            target[idx] += 1
        
        for i in range(k):
            idx = ord(s2[i]) - ord("a")
            window[idx] += 1
        
        matches = 0
        for i in range(26):
            if window[i] == target[i]:
                matches += 1 
        if matches == 26:
            return True
        
        left = 0
        for right in range(k, n):
            r_char = s2[right]
            r_idx = ord(r_char) - ord("a")

            before = window[r_idx]
            window[r_idx] += 1
            after = window[r_idx]
            if before == target[r_idx]:
                matches -= 1
            if after == target[r_idx]:
                matches += 1
            
            l_char = s2[left]
            l_idx = ord(l_char) - ord("a")

            before = window[l_idx]
            window[l_idx] -= 1
            after = window[l_idx]
            if before == target[l_idx]:
                matches -= 1
            if after == target[l_idx]:
                matches += 1

            left += 1
            if matches == 26:
                return True
                
        return False