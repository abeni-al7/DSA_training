class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['N'] * n for _ in range(m)]
        count = 0

        for x, y in guards:
            matrix[x][y] = 'G'
        for x, y in walls:
            matrix[x][y] = 'W'

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'G':
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i, j = r + dr, c + dc
                        while 0 <= i < m and 0 <= j < n and matrix[i][j] != 'W' and matrix[i][j] != 'G':
                            matrix[i][j] = 'P'
                            i += dr
                            j += dc

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'N':
                    count += 1

        return count
