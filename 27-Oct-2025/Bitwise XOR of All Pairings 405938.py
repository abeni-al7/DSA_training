# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_2 = 0
        for num in nums2:
            xor_2 ^= num
        
        xor_1 = 0
        for num in nums1:
            xor_1 ^= num
        
        if len(nums1) % 2 == 0:
            xor_2 = 0
        if len(nums2) % 2 == 0:
            xor_1 = 0
            
        return xor_1 ^ xor_2