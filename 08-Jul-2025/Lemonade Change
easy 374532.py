# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for bill in bills:
            if bill == 5:
                count[5] += 1
            elif bill == 10:
                count[10] += 1
                if count[5]:
                    count[5] -= 1
                else:
                    return False
            else:
                count[20] += 1
                if count[10] and count[5]:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True