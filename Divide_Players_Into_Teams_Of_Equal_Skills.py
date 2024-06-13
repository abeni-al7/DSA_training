class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        team = skill[l] + skill[r]
        answer = 0
        while l < r:
            if skill[l] + skill[r] != team:
                return -1
            answer += (skill[l] * skill[r])
            l += 1
            r -= 1
        return answer
            
        
