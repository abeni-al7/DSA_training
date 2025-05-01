class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(int)
        maximum = 0
        curr = 0
        l = 0
        for r in range(len(fruits)):
            types[fruits[r]] += 1
            curr += 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1
            maximum = max(maximum, r - l + 1)
        return maximum


        
