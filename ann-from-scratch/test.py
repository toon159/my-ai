import random
class NeuralNetwork:
    '''
    Doc?
    '''
    def init(self, x, y):
        self.input = x
        self.weight1 = random.random()
        self.weight2 = random.random()
        self.y = y
        self.output = y

    
    

'''
O   O
    O   O
O   O

2 > 3 > 1
in >>> out

'''

n = NeuralNetwork()