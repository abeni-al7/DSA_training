# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, rest = s.split("@")
            domain, tld = rest.split(".")
            masked = name[0].lower() + ("*" * 5) + name[-1].lower() + "@" +  domain.lower() + "." + tld.lower()
            return masked
        else:
            digit_count = 0
            digits = []
            for char in s:
                if char.isdigit():
                    digit_count += 1
                    digits.append(char)
            masked = ("*" * 3) + "-" + ("*" * 3) + "-" + "".join(digits[-4:])   
            if digit_count == 11:
                masked = "+*-" + masked
            elif digit_count == 12:
                masked = "+**-" + masked
            elif digit_count == 13:
                masked = "+***-" + masked
            return masked