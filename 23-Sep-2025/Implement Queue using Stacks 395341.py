# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.top >= len(self.stack):
            return -1
        val = self.stack[self.top]
        self.top += 1
        return val

    def peek(self) -> int:
        if self.top >= len(self.stack):
            return -1
        val = self.stack[self.top]
        return val

    def empty(self) -> bool:
        if self.top >= len(self.stack):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()