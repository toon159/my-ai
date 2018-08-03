import numpy as np 
import time
np.random.seed(1)

N_STATES = 5
ACTIONS = [0, 1]
MAX_EPISODES = 20


def build_q_table(n_states):
    table = {}
    for i in range(n_states):
        table[i] = [0, 0]
    return table


def choose_action(state, q_table):
    state_actions = q_table[state]
    if np.random.uniform() > 0.9 or state_actions == [0, 0]:
        action = np.random.choice(ACTIONS)
    else:
        if state_actions[0] < state_actions[1]:
            action = 1
        else:
            action = 0
    return action


def get_env_feedback(S, A):
    if A == 1:
        if S == N_STATES - 2:
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else: # left
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
        R = 0
    return S_, R


def update_env(S, episode, step_counter):
    for i in range(N_STATES):
        if i == S:
            print('o', end="")
        else:
            print('-', end="")
    print("T")
    time.sleep(0.05)
    

# MAIN
q_table = build_q_table(N_STATES)
for episode in range(50):
    print(q_table)
    step_counter = 0
    S = 0
    is_terminated = False
    update_env(S, episode, step_counter)
    while not is_terminated:
        A = choose_action(S, q_table)
        S_, R = get_env_feedback(S, A)
        print(q_table)
        q_predict = q_table[S][A]
        if S_ != 'terminal':
            if q_table[S_][0] > q_table[S_][1]:
                q_target = R + 0.9 * q_table[S_][0]
            else:
                q_target = R + 0.9 * q_table[S_][1]
        else:
            q_target = R
            is_terminated = True
        if A == 'left':
            q_table[S][0] += 0.1 * (q_target - q_predict)
        else:
            q_table[S][1] += 0.1 * (q_target - q_predict)
        S = S_

        update_env(S, episode, step_counter+1)
        step_counter += 1  