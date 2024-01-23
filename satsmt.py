from z3 import *


rows = 5
cols = 5


grid = [[Bool(f'cell_{i}_{j}') for j in range(cols)] for i in range(rows)]


solver = Solver()


solver.add(Not(grid[1][1]))  # Example: Wall at (1, 1)


goal_row, goal_col = 3, 3
solver.add(grid[goal_row][goal_col])


for i in range(rows):
    for j in range(cols):
        if i < rows - 1:
            
            solver.add(Implies(grid[i][j], grid[i + 1][j]))
        if j < cols - 1:
            
            solver.add(Implies(grid[i][j], grid[i][j + 1]))
        if i > 0:
            
            solver.add(Implies(grid[i][j], grid[i - 1][j]))
        if j > 0:
            
            solver.add(Implies(grid[i][j], grid[i][j - 1]))


if solver.check() == sat:
    model = solver.model()
    
    path = [(i, j) for i in range(rows) for j in range(cols) if is_true(model.eval(grid[i][j]))]
    print("Path to goal:", path)
else:
    print("No solution found.")
