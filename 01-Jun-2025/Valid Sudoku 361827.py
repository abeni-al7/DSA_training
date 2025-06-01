# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        three = set()

        # Check each row and col
        for i in range(9):
            for j in range(9):
                row = board[i][j]
                col = board[j][i]
                if (row != "." and row in rows) or (col != "." and col in cols):
                    return False
                rows.add(row)
                cols.add(col)
            rows = set()
            cols = set()

        # Check each 3x3
        i, j = 0, 0
        while i < 9:
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    current = board[k][l]
                    if current != "." and current in three:
                        return False
                    three.add(current)
            three = set()
            j += 3
            if j == 9:
                j = 0
                i += 3
        return True
