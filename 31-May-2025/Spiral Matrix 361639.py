# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        inbound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) not in visited

        i, j = 0, 0
        curr_dir = 0
        while inbound(i, j):
            result.append(matrix[i][j])
            visited.add((i, j))
            if not inbound(i + directions[curr_dir][0], j + directions[curr_dir][1]):
                curr_dir = (curr_dir + 1) % 4
            i += directions[curr_dir][0]
            j += directions[curr_dir][1]
        return result
        