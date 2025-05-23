# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        answer = ""
        while num:
            if num >= roman_dict["M"]:
                num -= roman_dict["M"]
                answer += "M"
            elif num >= 900:
                num -= 900
                answer += "CM"
            elif num >= roman_dict["D"]:
                num -= roman_dict["D"]
                answer += "D"
            elif num >= 400:
                num -= 400
                answer += "CD"
            elif num >= roman_dict["C"]:
                num -= roman_dict["C"]
                answer += "C"
            elif num >= 90:
                num -= 90
                answer += "XC"
            elif num >= roman_dict["L"]:
                num -= roman_dict["L"]
                answer += "L"
            elif num >= 40:
                num -= 40
                answer += "XL"
            elif num >= roman_dict["X"]:
                num -= roman_dict["X"]
                answer += "X"
            elif num >= 9:
                num -= 9
                answer += "IX"
            elif num >= roman_dict["V"]:
                num -= roman_dict["V"]
                answer += "V"
            elif num >= 4:
                num -= 4
                answer += "IV"
            else:
                num -= roman_dict["I"]
                answer += "I"
        
        return answer