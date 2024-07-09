class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-1 * (stack.pop() - stack.pop()))
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return int(stack[0])
