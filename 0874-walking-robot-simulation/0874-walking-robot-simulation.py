class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacleSet = set(map(tuple, obstacles))
        
        x = y = di = 0
        maxDistSquared = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                di = (di - 1) % 4
            elif cmd == -1:  # Turn right
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        maxDistSquared = max(maxDistSquared, x*x + y*y)
        
        return maxDistSquared
        