# Genetic Algorithm
# for Knapsack problem

import random
import numpy as np

# Item i has weight[i] and values[i]
ITEMS_NAMES = np.array(['drinking water', 'gaming laptop', 'canned food', 'torch', 'knife', 'phone'])
ITEMS_WEIGHTS = np.array([10, 15, 8, 5, 1, 2])
ITEMS_VALUES = np.array([8, 6, 11, 5, 3, 1])

WEIGHT_LIMIT = 30
MUTATION_RATE = 0.2

POP_SIZE = 100


# create pops array with random genes
def create_pops():
    pops = []
    for pop in range(POP_SIZE):
        genes = []
        for _ in range(len(ITEMS_VALUES)):
            genes.append(random.randint(0, 1))
        pops.append(genes)
    return pops


def cal_value(pops):
    pops_value = []
    pops = list(pops)
    # check bag value
    for gene in pops:
        total_weight = sum(gene * ITEMS_WEIGHTS)
        total_value = sum(gene * ITEMS_VALUES)
        # check if too heavy
        if total_weight > WEIGHT_LIMIT:
            pops_value.append(-1)
        else:
            pops_value.append(total_value)
    return pops_value


def show_summary(pops):
    pops_value = cal_value(pops)
    for i, pop in enumerate(pops, 1):
        pop = np.array(pop)
        pop_value = pops_value[i - 1]
        pop_weight = sum(pop * ITEMS_WEIGHTS)
        picked = pop == 1
        print(f'No.{i} has {pop_weight} weight and gets {pop_value} scores by picked {ITEMS_NAMES[picked]}')


def select_top_2(pops):
    # sort
    pops_value = np.array(cal_value(pops))  # turn array of values into np.array
    pops_value.sort()  # sort them so the most value will be on the right
    pops_value = pops_value.tolist()  # back to the list
    # pop
    max1_value = pops_value.pop()  # pop the most score
    max2_value = pops_value.pop()  # pop the second most score
    # back to ori state
    pops_value = cal_value(pops)  # turn array of values into previous array before the pop
    # get the genes
    max1_index = pops_value.index(max1_value)  # get index
    max2_index = pops_value.index(max2_value)  # get index
    max1_gene = pops[max1_index]  # get the 1st gene
    max2_gene = pops[max2_index]  # get the 2nd gene
    pops_list = (max1_gene, max2_gene)  # pack them into a tuple
    return pops_list


def flip_bit(l, pos):
    bit = l[pos]
    if bit == 0:
        l[pos] = 1
    else:
        l[pos] = 0
    return list


def mutation(pops):
    print('mutation', type(pops), pops)
    for pop in pops:
        if np.random.rand() < MUTATION_RATE:
            ran_num = np.random.randint(len(pop))
            pop = flip_bit(pop, ran_num)
            print(f"mutate {pop}")
    return pops


def single_point_crossover(parents):
    p1 = list(parents[0])
    p2 = list(parents[1])
    for i in range(3):
        p1[i], p2[i] = p2[i], p1[i]
    return p1, p2


def two_point_crossover(parents):
    p1 = list(parents[0])
    p2 = list(parents[1])
    for j in range(3):
        for i in range(2):
            if j == 1:
                continue
            else:
                x = j * 2 + i
                p1[x], p2[x] = p2[x], p1[x]
    return p1, p2


def crossover(parents):
    temp = list(parents)
    c1, c2 = list(single_point_crossover(temp))
    c3, c4 = list(two_point_crossover(temp))
    children = parents[0], parents[1], c1, c2, c3, c4
    return children


def to_next_gen(top):
    new_pops = top
    new_pops = crossover(new_pops)
    new_pops = mutation(new_pops)
    return new_pops


pops = create_pops()
pops_value = cal_value(pops)
show_summary(pops)


for i in range(0):
    print(f'generation {i+2} : ')
    top2 = select_top_2(pops)
    pops_ = to_next_gen(top2)
    pops_value = cal_value(pops_)
    show_summary(pops_)
    pops = pops_
    high_score = max(pops_value)
    if high_score > 28:
        break
    print('*' * 30, f'The highest score is {high_score} !!!!', '*' * 30, '\n')
