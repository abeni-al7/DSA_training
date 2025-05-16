# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask_list = []
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord("a")))
            mask_list.append(mask)
        
        max_prod = 0
        for i in range(len(mask_list)):
            for j in range(i + 1, len(mask_list)):
                if mask_list[i] & mask_list[j] == 0:
                    prod = len(words[i]) * len(words[j])
                    max_prod = max(max_prod, prod)
        return max_prod