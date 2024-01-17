def bfs(robot_position, goal_position, grid):
    queue = [robot_position]
    visited = set()

    while queue:
        current_position = queue.pop(0)

        if current_position == goal_position:
            return "Goal reached!"

        if current_position not in visited:
            visited.add(current_position)
            neighbors = get_neighbors(current_position, grid)
            queue.extend(neighbors)

    return "Goal not reachable."
