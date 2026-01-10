class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        current = 1
        for i in range(len(nums)):
            product.append(current)
            current *= nums[i]
        
        current = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= current
            current *= nums[i]
        return product
        
        return [prefix[i] * suffix[j] for i in range(len(nums)) for j in range(len(nums) - 1, -1, -1)]
"""
nums = [1, 2, 3, 4]
after = [24, 12, 4, 1]
product_back = [1, 1, 2, 6]
"""