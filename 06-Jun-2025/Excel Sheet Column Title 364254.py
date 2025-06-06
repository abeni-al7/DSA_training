# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        initial = defaultdict(str)
        for i in range(1, 27):
            initial[i] = chr(i + ord("A") - 1)
        
        digits = []
        while columnNumber:
            if columnNumber % 26 != 0:
                digits.append(columnNumber % 26)
                columnNumber //= 26
            else:
                digits.append(26)
                columnNumber //= 26
                columnNumber -= 1  
        digits.reverse()
        return "".join(list(initial[i] for i in digits))
        