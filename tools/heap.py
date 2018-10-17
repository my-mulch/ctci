from misc import swap
import numpy as np

class Heap():

    def __init__(self, data):
        self.data = data
        self.size = len(self.data)
    
    @staticmethod
    def build_max_heap(heap):
        # from i / 2 downto 0 as everything beyond are already leaves
        # and thus satisfy the max heap property
        for i in reversed(range(heap.size // 2)): 
            Heap.max_heapify(heap, i)

    @staticmethod
    def max_heapify(heap, i):
        if i < heap.size // 2:
            lci = 2 * i + 1
            rci = 2 * i + 2
            
            lc = heap.data[lci]
            rc = heap.data[rci] if rci < heap.size else lc
            ci = heap.data[i]
            
            max_i = lci if lc >= rc else rci
            max_c = heap.data[max_i]

            if ci >= max_c:
                return
        
            swap(heap.data, i, max_i)
            Heap.max_heapify(heap, max_i)
            
    def extract_max(self):
        max_val = self.data[0]
        
        self.data[0] = self.data[self.size - 1]
        self.size -= 1

        Heap.max_heapify(self, 0)
        return max_val
    
    def sort(self):
        while self.size:
            yield self.extract_max()

heap = Heap(np.random.randn(100000).tolist())
Heap.build_max_heap(heap)
list(heap.sort())