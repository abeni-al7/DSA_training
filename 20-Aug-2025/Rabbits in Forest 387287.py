# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        freq = Counter(answers)

        for k, v in freq.items():
            if k + 1 >= v:
                count += k + 1
            else:
                while v > 0:
                    v -= k + 1
                    count += k + 1
                    
                
        return count