# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        current = 1
        for i in range(len(nums)):
            if i == 0:
                prefix_product.append(1)
            else:
                current *= nums[i - 1]
                prefix_product.append(current)
        
        suffix_product = [0] * len(nums)
        current = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix_product[i] = 1
            else:
                current *= nums[i + 1]
                suffix_product[i] = current
        
        output = []
        for i in range(len(nums)):
            output.append(prefix_product[i] * suffix_product[i])
        return output