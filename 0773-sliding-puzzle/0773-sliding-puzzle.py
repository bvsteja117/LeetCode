class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1,2,3],[4,5,0]]
        def board_to_tuple(b):
            return tuple(tuple(row) for row in b)
        
        # Get Manhattan distance heuristic
        def manhattan_distance(board):
            distance = 0
            board_dict = {num: (i, j) for i, row in enumerate(board) 
                         for j, num in enumerate(row)}
            target_dict = {num: (i, j) for i, row in enumerate(target) 
                          for j, num in enumerate(row)}
            
            for num in range(1, 6):
                bx, by = board_dict[num]
                tx, ty = target_dict[num]
                distance += abs(bx - tx) + abs(by - ty)
            return distance
        
        # Get next possible states
        def get_next_states(board):
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
            states = []
            
            # Find empty tile (0)
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        empty_pos = (i, j)
                        break
                else:
                    continue
                break
            
            # Try all possible moves
            for dx, dy in moves:
                new_x, new_y = empty_pos[0] + dx, empty_pos[1] + dy
                
                if 0 <= new_x < 2 and 0 <= new_y < 3:
                    # Create new board state
                    new_board = [row[:] for row in board]
                    # Swap tiles
                    new_board[empty_pos[0]][empty_pos[1]] = new_board[new_x][new_y]
                    new_board[new_x][new_y] = 0
                    states.append(new_board)
            
            return states
        
        # Check if puzzle is solvable
        def is_solvable(board):
            # Flatten the board
            flat = [num for row in board for num in row if num != 0]
            
            # Count inversions
            inversions = 0
            for i in range(len(flat)):
                for j in range(i + 1, len(flat)):
                    if flat[i] > flat[j]:
                        inversions += 1
            
            return inversions % 2 == 0
        
        # Main solution using A* search
        if not is_solvable(board):
            return -1
        
        # Priority queue for A* search: (f_score, moves, board)
        pq = [(0, 0, board)]
        visited = {board_to_tuple(board): 0}  # board_state: moves
        heapq.heapify(pq)
        
        while pq:
            f, moves, current = heapq.heappop(pq)
            
            # Check if we reached the target
            if current == target:
                return moves
            
            # Generate next possible states
            for next_state in get_next_states(current):
                next_tuple = board_to_tuple(next_state)
                
                # If we haven't visited this state or found a better path
                if next_tuple not in visited or visited[next_tuple] > moves + 1:
                    visited[next_tuple] = moves + 1
                    h_score = manhattan_distance(next_state)
                    f_score = moves + 1 + h_score
                    heapq.heappush(pq, (f_score, moves + 1, next_state))
        
        return -1  # No solution found