class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        order = 1
        digitSum = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                x += int(order * digit)
                digitSum += digit
                order *= 10
            n //= 10
        return x * digitSum
