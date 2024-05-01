class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        print(nums1_count, nums2_count)
        ans = []
        visited = set()
        if len(nums1) < len(nums2):
            for num in nums1:
                if num in nums2_count and num not in visited:
                    visited.add(num)
                    ans.extend([num] * min(nums1_count[num], nums2_count[num]))
                print(ans)
        else:
            for num in nums2:
                if num in nums1_count and num not in visited:
                    ans.extend([num] * min(nums1_count[num], nums2_count[num]))
                    visited.add(num)
                print(ans)
        return ans
