from z3 import *

# Define grid size
rows = 5
cols = 5

# Create boolean variables for each grid cell
grid = [[Bool(f'cell_{i}_{j}') for j in range(cols)] for i in range(rows)]

# Create Z3 solver
solver = Solver()

# Add constraints for obstacles or walls (setting cells to False)
solver.add(Not(grid[1][1]))  # Example: Wall at (1, 1)

# Add constraints for the goal state (setting goal cell to True)
goal_row, goal_col = 3, 3
solver.add(grid[goal_row][goal_col])

# Add transition constraints (allowing the robot to move to adjacent cells)
for i in range(rows):
    for j in range(cols):
        if i < rows - 1:
            # Allow moving down (current cell implies next cell)
            solver.add(Implies(grid[i][j], grid[i + 1][j]))
        if j < cols - 1:
            # Allow moving right (current cell implies next cell)
            solver.add(Implies(grid[i][j], grid[i][j + 1]))
        if i > 0:
            # Allow moving up (current cell implies previous cell)
            solver.add(Implies(grid[i][j], grid[i - 1][j]))
        if j > 0:
            # Allow moving left (current cell implies previous cell)
            solver.add(Implies(grid[i][j], grid[i][j - 1]))

# Solve the SMT problem
if solver.check() == sat:
    model = solver.model()
    # Extract the path from the model
    path = [(i, j) for i in range(rows) for j in range(cols) if is_true(model.eval(grid[i][j]))]
    print("Path to goal:", path)
else:
    print("No solution found.")
