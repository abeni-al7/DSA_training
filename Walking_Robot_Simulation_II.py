class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [(0, 0)]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dlabels = ["East", "North", "West", "South"]
        self.dir = 0

    def step(self, num: int) -> None:
        num %= (self.width - 1 + self.height - 1) * 2
        if num == 0:
            num += (self.width - 1 + self.height - 1) * 2
        for _ in range(num):
            nx, ny = self.pos[-1][0] + self.directions[self.dir][0], self.pos[-1][1] + self.directions[self.dir][1]
            while not (0 <= nx < self.width and 0 <= ny < self.height):
                self.dir = (self.dir + 1) % 4
                nx, ny = self.pos[-1][0] + self.directions[self.dir][0], self.pos[-1][1] + self.directions[self.dir][1]
            self.pos.append((nx, ny))

    def getPos(self) -> List[int]:
        return list(self.pos[-1])

    def getDir(self) -> str:
        return self.dlabels[self.dir]
