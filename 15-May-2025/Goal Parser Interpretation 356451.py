# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        for i, char in enumerate(command):
            if char == "G":
                interpreted += "G"
            elif char == ")" and command[i - 1] == "(":
                interpreted += "o"
            elif char == ")":
                interpreted += "al"
        return interpreted