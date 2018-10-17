from misc import swap

class Heap():

    def __init__(self, data):
        self.data = data
        self.leaf_line = len(self.data) // 2

        for i in reversed(range(self.leaf_line)):
            self.max_heapify(i)
        
        print(self.data)
    
    def max_heapify(self, i):
        if i < self.leaf_line:
            lci = 2 * i + 1
            rci = 2 * i + 2
            
            lc = self.data[lci]
            rc = self.data[rci]
            ci = self.data[i]
            
            max_i = lci if lc >= rc else rci
            max_c = self.data[max_i]

            if ci >= max_c:
                return
        
            swap(self.data, i, max_i)
            self.max_heapify(max_i)
            




Heap([10,17,3,4,2,6,4])

