class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        newgrid = []
        for i in range(len(grid) - 2):
            colgrid = []
            for j in range(len(grid) - 2):
                colgrid.append(self.maxvalue(grid, i, j))
            newgrid.append(colgrid)
        return newgrid
    
    def maxvalue(self, grid, row, col):
        maxval = float('-inf')
        for i in range(row, row+3):
            for j in range(col, col+3):
                maxval = max(maxval, grid[i][j])
        return maxval
