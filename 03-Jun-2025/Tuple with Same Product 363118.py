# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product = nums[i] * nums[j]
                if i not in count[product] and j not in count[product]:
                    count[product].extend([i, j])
        result = 0
        for val in count.values():
            n = len(val)
            pairs = n // 2
            if n > 2:
                result += (pairs) * (4 + (pairs - 2) * 4)
        return result