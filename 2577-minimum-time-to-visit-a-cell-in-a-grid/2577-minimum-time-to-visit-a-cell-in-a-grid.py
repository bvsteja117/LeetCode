from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        pq = [(0, 0, 0)]  # (time, row, col)
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            if row == m - 1 and col == n - 1:
                return time
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if (0 <= new_row < m and 0 <= new_col < n and 
                    (new_row, new_col) not in visited):
                    
                    wait_time = max(0, grid[new_row][new_col] - time - 1)
                    
                    if wait_time % 2 != 0 and grid[new_row][new_col] > time + 1:
                        wait_time += 1
                    
                    new_time = time + wait_time + 1
                    heapq.heappush(pq, (new_time, new_row, new_col))
        
        return -1