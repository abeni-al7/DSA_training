# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            freq[num % k] += 1
        
        for i in range(1, k):
            if i == k - i and freq[i] % 2:
                return False

            if freq[i] != freq[k - i]:
                return False
        return True

