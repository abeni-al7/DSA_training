# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = set()
        for num in nums:
            if nums.count(num) == 2:
                ans.add(num)
        return list(ans)