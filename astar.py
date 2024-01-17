def astar(robot_position, goal_position, grid):
    open_set = PriorityQueue()
    open_set.put((0, robot_position))  # (f_score, position)
    came_from = {}
    g_score = {robot_position: 0}

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal_position:
            return reconstruct_path(came_from, goal_position)

        neighbors = get_neighbors(current, grid)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + cost(current, neighbor)

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal_position)
                open_set.put((f_score, neighbor))
                came_from[neighbor] = current

    return "Goal not reachable."
