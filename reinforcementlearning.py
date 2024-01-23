import numpy as np


num_states = 100  # Adjust based on the size of your state space
num_actions = 4  # Assuming four possible actions (up, down, left, right)
Q = np.zeros((num_states, num_actions))


alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration-exploitation trade-off


state_space = range(num_states)
action_space = range(num_actions)


def get_reward(state, action):
    
    goal_state = 90
    if state == goal_state and action == 2:  # Assuming action 2 is moving right
        return 10
    else:
        return -1  # A small negative reward for other actions

def get_next_state(state, action):
    
    if action == 0:  # Move up
        return max(state - 10, 0)  # Ensure not going above the top row
    elif action == 1:  # Move down
        return min(state + 10, num_states - 1)  # Ensure not going below the bottom row
    elif action == 2:  # Move left
        return max(state - 1, 0) if state % 10 != 0 else state  # Ensure not crossing left boundary
    elif action == 3:  # Move right
        return min(state + 1, num_states - 1) if (state + 1) % 10 != 0 else state  # Ensure not crossing right boundary


num_episodes = 1000

for episode in range(num_episodes):
    
    current_state = np.random.choice(state_space)

    
    while True:
        
        if np.random.rand() < epsilon:
            selected_action = np.random.choice(action_space)
        else:
            selected_action = np.argmax(Q[current_state, :])

        
        next_state = get_next_state(current_state, selected_action)
        reward = get_reward(current_state, selected_action)

        
        Q[current_state, selected_action] = (1 - alpha) * Q[current_state, selected_action] + \
                                            alpha * (reward + gamma * np.max(Q[next_state, :]))

        
        current_state = next_state

        # Checking if the goal state is reached (for simplicity, assuming state 90 is the goal)
        if current_state == 90:
            break
