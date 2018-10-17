from misc import swap

class Heap():

    def __init__(self, data):
        self.heap = Heap.build_max_heap(data)
    
    @staticmethod
    def build_max_heap(data):
        # from i / 2 downto 0 as everything beyond are already leaves
        # and thus satisfy the max heap property
        for i in reversed(range(len(data) // 2)): 
            Heap.max_heapify(data, i)
        
        return data

    @staticmethod
    def max_heapify(arr, i):
        if i < len(arr) // 2:
            lci = 2 * i + 1
            rci = 2 * i + 2
            
            lc = arr[lci]
            rc = arr[rci]
            ci = arr[i]
            
            max_i = lci if lc >= rc else rci
            max_c = arr[max_i]

            if ci >= max_c:
                return
        
            swap(arr, i, max_i)
            Heap.max_heapify(arr, max_i)
            




print(Heap([10,17,3,4,2,6,4]).heap)

