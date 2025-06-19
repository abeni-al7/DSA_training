# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        uniques = set()
        l = 0
        max_fruits = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            uniques.add(fruits[r])
            while len(uniques) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    uniques.remove(fruits[l])
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits