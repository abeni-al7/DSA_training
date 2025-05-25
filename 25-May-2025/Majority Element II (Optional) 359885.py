# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for k, v in count.items():
            if v > len(nums) / 3:
                ans.append(k)
        return ans