class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        low_digit, high_digit = len(str(low)), len(str(high))

        for digit in range(low_digit, high_digit + 1):
            for start in range(1, 9):
                if start + digit > 10:
                    break
                num = start
                prev = start
                for i in range(digit - 1):
                    num *= 10
                    prev += 1
                    num += prev
                if low <= num <= high:
                    res.append(num)
        return res