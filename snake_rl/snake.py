class snake():
    pos = []
    head = -1
    tail = -1
    body = []


    def __init__(self, pos):
        self.pos = pos


    def to5x5(self, number):
        row = int(number / 5)
        col = number % 5
        return [row, col]


    def iden_structure(self, pos):
        head = -1
        tail = -1
        body = []
        if len(pos) == 1:
            head = pos[0]
        elif len(pos) == 2:
            head = pos[0]
            tail = pos[1]
        else:
            head = pos.pop(0)
            tail = pos.pop()
            body = pos
        return head, tail, body

    def move(self, pos, action):
        head, tail, body = iden_structure(pos)
        if action == 0: # up
            pass
        elif action == 1: # down
            pass
        elif action == 2: # left
            pass
        elif action == 3: # right
            pass