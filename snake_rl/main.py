import time as t
import numpy as np
import pandas as pd
import snake

TABLE_WIDTH = 5
ACTIONS = [0, 1, 2, 3] # 0 up, 1 down, 2 left, 3 right


def add_food(state):
    empty = []
    index = 0
    # find all empty space
    for i in state:
        if i == 0:
            empty.append(index)
        index += 1
    food_index = np.random.choice(empty) # then select randomly
    state[food_index] = 3 # set the selected to be 3
    return state


def init_state():
    state = np.zeros((25,), dtype=int)
    state[12] = 1
    state = add_food(state)
    print(state) # temp
    return state


def choose_action(state, q_table, last_action):
    actions = set(ACTIONS) - last_action
    # find index of highest q value at the current state
    if state in tuple(q_table):
        actions_values = set(q_table[state] - last_action)
        max_actions_value = np.array(actions_values).max()
        max_actions_index = q_table[state].index(max_actions_value)
        action = max_actions_index
    else:
        action = np.random.choice(list(actions))
    return action


def to5x5(number):
    row = int(number / 5)
    col = number % 5
    return [row, col]


def body_5x5(state):
    i = [i for i, j in enumerate(state) if 2 in state]
    print(i)
    l_ = []
    for i in l:
        l_.append(to5x5(i))
    return l_

'''
def get_env_feedback(state, action, snake):
    if len(snake) == 1: # only head
        if action == 0:
    elif len(snake) == 2: # only head and tail; no body
    body = state == 2
    b_index = []
    for i, j in enumerate(body):
        if j == True:
            b_index.append(i)
    print(b_index)
    print(body)
    s = [state]
    print(s.index(0).all())
    state_ = state.reshape(5, 5) # state_ is a reshape version
    reward = -0.1

    pos_head = 
    pos_body = 
    pos_food = 
    pos_tail = 
    for row in range(TABLE_WIDTH):
        for col in range(TABLE_WIDTH):
            if [row, col] == pos_food:
                pass
            elif [row, col] == pos_body:
                pass
            else:
                pass

    new_state = state_.reshape(1,)

    return new_state, reward
'''

def update_env(state):
    state_ = state.reshape(5, 5)
    # print the env
    for row in range(TABLE_WIDTH):
        for col in range(TABLE_WIDTH):
            val = state_[row][col]
            if val == 0: # empty
                print('.', end=' ')
            elif val == 1: # head
                print('*', end=' ')
            elif val == 2: # body
                print('x', end=' ')
            elif val == 3: # food
                print('o', end=' ')
            elif val == 4: # tail
                print('t')
        print('')



def main():
    q_table = {}
    snake = snake([12])
    last_action = set([])
    state = init_state()
    update_env(state)
    game_over = False
    while not game_over:
        action = choose_action(state, q_table, last_action)
        # state_, reward = get_env_feedback(state, action, snake)
        this_q = q_table[state][action]
        game_over = True

        #         if S_ != 'terminal':
        #     if q_table[S_][0] > q_table[S_][1]:
        #         q_target = R + 0.9 * q_table[S_][0]
        #     else:
        #         q_target = R + 0.9 * q_table[S_][1]
        # else:
        #     q_target = R
        #     is_terminated = True
        # if A == 'left':
        #     q_table[S][0] += 0.1 * (q_target - q_predict)
        # else:
        #     q_table[S][1] += 0.1 * (q_target - q_predict)
        # S = S_


if __name__ == "__main__":
    main()
