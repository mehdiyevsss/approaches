def dfs(robot_position, goal_position, grid, visited):
    if robot_position == goal_position:
        return "Goal reached!"

    if robot_position not in visited:
        visited.add(robot_position)
        neighbors = get_neighbors(robot_position, grid)

        for neighbor in neighbors:
            result = dfs(neighbor, goal_position, grid, visited)
            if result == "Goal reached!":
                return result

    return "Goal not reachable."
