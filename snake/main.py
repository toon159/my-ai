import numpy as np
import pandas as pd
import snake as sn
import time as t

TABLE_WIDTH = 5
ACTIONS = ['u', 'd', 'l', 'r']

def init_state():
    state = np.zeros((5, 5), dtype=int)
    state[2][2] = 1
    return state

def add_food(state):
    empty = []
    for i in state:
        print(i)
    return state


def choose_action(state, q_table, last_action):
    actions = set(ACTIONS) - last_action
    # find index of highest q value at the current state
    if state in q_table:
        actions_values = set(q_table[state] - last_action)
        max_actions_value = np.array(actions_values).max()
        max_actions_index = q_table[state].index(max_actions_value)
        action = max_actions_index
    else:
        action = np.random.choice(actions)
    return action


def get_env_feedback(state, action):
    state_ = state
    reward = -0.1
    return state_, reward


def update_env(state):
    state[0][0] = 2
    state[0][1] = 2
    state[0][2] = 1
    state[4][2] = 3
    # print the env
    for row in range(TABLE_WIDTH):
        for col in range(TABLE_WIDTH):
            val = state[row][col]
            if val == 0: # empty
                print('.', end=' ')
            elif val == 1: # head
                print('*', end=' ')
            elif val == 2: # body
                print('x', end=' ')
            elif val == 3: # food
                print('o', end=' ')
        print('')



def main():
    q_table = {}
    last_action = set([])
    state = init_state()
    update_env(state)
    game_over = False
    while not game_over:
        action = choose_action(state, q_table, last_action)
        state_, reward = get_env_feedback(state, action)

        game_over = True



if __name__ == "__main__":
    main()