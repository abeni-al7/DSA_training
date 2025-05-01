class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for r in range(rows + 1)]
        for r in range(rows):
            total = 0
            for c in range(cols):
                above = self.prefix[r][c+1]
                total += matrix[r][c]
                self.prefix[r+1][c+1] += total
                self.prefix[r+1][c+1] += above
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 +1
        total = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        topLeft = self.prefix[row1 - 1][col1 - 1]
        answer = total - above - left + topLeft
        return answer
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
