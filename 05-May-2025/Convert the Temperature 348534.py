# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Calculate kelvin value and store it
        kelvin = celsius + 273.15
        # Calculate Fahrenheit and store it
        fahrenheit = celsius * 1.80 + 32.00
        # Return the values in an array
        return [kelvin, fahrenheit]