# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1