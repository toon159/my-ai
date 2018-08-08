ListOBJ = [[1, 1, 1, 1], [0, 0, 0, 0]]

for countList in range(2):
    _lenA2_ = len(ListOBJ[countList])
    i = 0
    newList = []
    a = ListOBJ[countList]

    while i < _lenA2_/2:
        _a_ = a.pop()
        newList.append(_a_)
        i += 1
    ListOBJ.append(newList)


print(ListOBJ, '\n', newList)