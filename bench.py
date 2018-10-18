from tools.bst import BST
from tools.heap import Heap

import numpy as np
import time



heap = Heap(np.random.randn(100000).tolist())
start_time = time.time()
Heap.build_max_heap(heap)
list(heap.sort())
print(time.time() - start_time, "seconds")
