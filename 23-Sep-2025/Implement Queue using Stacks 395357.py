# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.write = []
        self.read = []

    def push(self, x: int) -> None:
        self.write.append(x)
    
    def _transfer(self) -> None:
        if not self.read:
            while self.write:
                self.read.append(self.write.pop())

    def pop(self) -> int:
        self._transfer()
        return self.read.pop()

    def peek(self) -> int:
        self._transfer()
        return self.read[-1]

    def empty(self) -> bool:
        return len(self.read) + len(self.write) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()