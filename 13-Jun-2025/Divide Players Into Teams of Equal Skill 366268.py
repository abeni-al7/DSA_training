# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill_sum = set()
        skill.sort()

        l, r = 0, len(skill) - 1
        chemistry = 0
        while l < r:
            total = skill[l] + skill[r]
            skill_sum.add(total)
            if len(skill_sum) > 1:
                return -1
            product = skill[l] * skill[r]
            chemistry += product
            l += 1
            r -= 1
        return chemistry
            