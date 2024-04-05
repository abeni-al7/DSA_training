class Solution:
    def interpret(self, command: str) -> str:
        message = ""
        for i in range(len(command)):
            if command[i] == 'G':
                message += 'G'
            elif command[i] == '(' and i + 1 < len(command):
                if command[i + 1] == ')':
                    message += 'o'
                else:
                    message += 'al'
        return message
