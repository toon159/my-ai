import numpy as np # np.random :)
import time # to slow the output

ACTIONS = ['u', 'd', 'l', 'r']
np.random.seed(1)


# build q_table 
# {(0, 0): [0, 0, 0, 0],
#  (0, 1): [0, 0, 0, 0],
#  ...}
def build_q_table():
    q_table = {}
    for row in range(5):
        for col in range(5):
            q_table[(col, row)] = [0,0,0,0]
    return q_table


# return an action base on the most q value at the state
def choose_action(state, q_table, actions):
    all_state_action = q_table[state]
    max_index = index_of_maximum_value(all_state_action)
    if np.random.rand() < 0.1:
        action = actions[np.random.randint(4)]
    else:
        action = actions[max_index]
    return action

# return an index of the most value in the provided list
def index_of_maximum_value(li):
    max_value = li[0]
    max_index = 0
    for value in li:
        if value > max_value:
            max_value = value
            max_index = li.index(value)
    return max_index

# return predicted state and predicted action
def get_env_feedback(S, A):
    S_ = list(S)
    R = -0.1
    if A == 'u':
        S_[1] = S[1] - 1
    elif A == 'd':
        S_[1] = S[1] + 1
    elif A == 'l':
        S_[0] = S[0] - 1  
    elif A == 'r':
        S_[0] = S[0] + 1
    # if reach trap
    if S_ == [2, 1] or S_ == [3, 1]:
        S_ = 'trap'
        R = -1
    # if reach goal
    elif S_ == [4, 0]:
        S_ = 'goal'
        R = 1
    else:
        # if reach wall (l, r)
        if S_[0] < 0 or S_[0] > 4:
            S_[0] = S[0]
            R = -0.2
        # if reach wall (u, d)
        if S_[1] < 0 or S_[1] > 4:
            S_[1] = S[1]
            R = -0.2
    S_ = tuple(S_)
    return S_, R


# show the environment on the screen
def update_env(S):
    for row in range(5):
        for col in range(5):
            if col == S[0] and row == S[1]:
                print("o", end="")
            elif col == 4 and row == 0:
                print("T", end="")
            elif (col == 2 or col == 3) and row == 1:
                print("X", end="")
            else:
                print("-", end="")
        print()



# to return the index of the value in the list
def index_in_list(li, value):
    
    return


def main():
    # state starts at (0, 4)
    state = (0, 4)
    q_table = build_q_table()

    for i in range(20):
        state = (0, 4)
        is_game_over = False
        turn = 0
        while not is_game_over:
            turn += 1
            action = choose_action(state, q_table, ACTIONS)
            new_state, reward = get_env_feedback(state, action)

            action_index = ACTIONS.index(action)
            q_table[state][action_index] = 0.1 * reward



            #########################
            update_env(state)
            print(state, action, new_state, reward)
            print(q_table)
            time.sleep(0.2)
            state = new_state
            if state == tuple('trap') or state == tuple('goal') or turn > 19:
                is_game_over = True
        print(f"-------- game '{i + 1}' over after '{turn}' turns passed --------")
        time.sleep(2)


if __name__ == "__main__":
    main()
