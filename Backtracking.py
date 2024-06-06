goal_state = [[1, 2, 3],
              [5, 8, 6],
              [7, 0, 4]]

# Function to check if the current state matches the goal state
def is_goal_state(state):
    return state == goal_state

# Function to find the next possible moves given the current state
def find_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                # Check if moving left is possible
                if j > 0:
                    moves.append((i, j-1))
                # Check if moving right is possible
                if j < 2:
                    moves.append((i, j+1))
                # Check if moving up is possible
                if i > 0:
                    moves.append((i-1, j))
                # Check if moving down is possible
                if i < 2:
                    moves.append((i+1, j))
    return moves

# Function to perform a move and update the current state
def make_move(state, move):
    i, j = move[0], move[1]
    new_state = [row[:] for row in state]  # Create a copy of the current state
    # Swap the empty space (0) with the selected tile
    new_state[i][j], new_state[empty_row][empty_col] = new_state[empty_row][empty_col], new_state[i][j]
    return new_state

# Function to solve the sliding puzzle using backtracking
def solve_puzzle(state, path):
    if is_goal_state(state):
        return True, path
    possible_moves = find_possible_moves(state)
    for move in possible_moves:
        new_state = make_move(state, move)
        if solve_puzzle(new_state, path + [move]):
            return True, path
    return False, []

# Example usage
initial_state = [[1, 2, 3],
                 [5, 6, 0],
                 [7, 8, 4]]
empty_row, empty_col = 1, 1  # Position of the empty space

found_solution, solution_path = solve_puzzle(initial_state, [])
if found_solution:
    print("Solution Found!")
    for move in solution_path:
        print("Move:", move)
else:
    print("No solution found.")