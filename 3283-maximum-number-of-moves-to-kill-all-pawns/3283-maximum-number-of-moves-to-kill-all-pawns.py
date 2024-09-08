from collections import deque
from functools import lru_cache
from typing import List

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        positions = [(kx, ky)] + positions  # Include knight's start position as position 0
        n = len(positions)
        
        # Precompute the shortest paths between all pairs of positions using BFS
        def bfs(start_idx):
            x, y = positions[start_idx]
            dist = [[float('inf')] * 50 for _ in range(50)]
            dist[x][y] = 0
            queue = deque([(x, y, 0)])
            
            while queue:
                x, y, d = queue.popleft()
                for dx, dy in knight_moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and dist[nx][ny] == float('inf'):
                        dist[nx][ny] = d + 1
                        queue.append((nx, ny, d + 1))
            return dist

        # Distance matrix between all positions
        dist_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            dist_from_i = bfs(i)
            for j in range(n):
                xj, yj = positions[j]
                dist_matrix[i][j] = dist_from_i[xj][yj]

        # Memoization for dp
        @lru_cache(None)
        def dp(mask, i, isAlice):
            if mask == 0:
                return 0

            if isAlice:
                max_moves = 0
                for j in range(1, n):
                    if mask & (1 << (j - 1)):
                        next_mask = mask & ~(1 << (j - 1))
                        max_moves = max(max_moves, dist_matrix[i][j] + dp(next_mask, j, False))
                return max_moves
            else:
                min_moves = float('inf')
                for j in range(1, n):
                    if mask & (1 << (j - 1)):
                        next_mask = mask & ~(1 << (j - 1))
                        min_moves = min(min_moves, dist_matrix[i][j] + dp(next_mask, j, True))
                return min_moves

        # All pawns are present initially, represented as a bitmask
        initial_mask = (1 << (n - 1)) - 1
        return dp(initial_mask, 0, True)
