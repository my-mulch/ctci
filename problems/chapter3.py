import math

class MinStack():

    def __init__(self):
        self.min = math.inf
        
        self.prev_mins = []
        self.stack = []
    
    def push(self, data):
        if data < self.min:
            self.min = data
            self.prev_mins.append(self.min)
        
        self.stack.append(data)
    
    def pop(self):
        popped = self.stack.pop()
        
        if popped  == self.prev_mins[-1]:
            self.prev_mins.pop()
            self.min = self.prev_mins[-1]
        
        return popped

