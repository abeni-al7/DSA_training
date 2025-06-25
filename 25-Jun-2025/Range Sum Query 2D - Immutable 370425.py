# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                top = self.prefix[i][j + 1]
                left = self.prefix[i + 1][j]
                top_left = self.prefix[i][j]
                val = matrix[i][j]
                self.prefix[i + 1][j + 1] = top + left - top_left + val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        top = self.prefix[r1 - 1][c2]
        left = self.prefix[r2][c1 - 1]
        top_left = self.prefix[r1 - 1][c1 - 1]
        val = self.prefix[r2][c2]
        return val - top - left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)