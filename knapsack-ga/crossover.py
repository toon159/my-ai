def flip_bit(l, pos):
    bit = l[pos]
    if bit == 0:
        l[pos] = 1
    else:
        l[pos] = 0
    return list

def s(parents):
    p1 = list(parents[0])
    p2 = list(parents[1])

    for i in range(3):
        p1[i], p2[i] = p2[i], p1[i]
    return p1, p2

def single_point_crossover(l):
    # for i in range(2):
    a = []
    b = []
    for i in range(2):
        a.append(l[0][i])
        b.append(l[1][i])

    for i in range(2):
        a.append(l[1][i+2])
        b.append(l[0][i+2])

    r = l, a, b

    return r


parents = [[1, 1, 1, 1], [0, 0, 0, 0]]

k1 = list(parents)
k = single_point_crossover(k1)
# print(k)

k2 = list(parents)
s = s(k2)
print(s)

print(k1 is parents)
