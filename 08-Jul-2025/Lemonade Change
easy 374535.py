# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1

            elif bill == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True