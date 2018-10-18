from tools.algorithms.sort import insertion_sort, insertion_sort_bin, heap_sort, merge_sort

import numpy as np
from timeit import Timer

arr = np.random.randint(0,20,1000000)

timer, label = Timer(lambda: insertion_sort(arr.tolist())), 'insertion-reg'
print(timer.timeit(1),label)

timer, label = Timer(lambda: insertion_sort_bin(arr.tolist())), 'insertion-bin'
print(timer.timeit(1),label)

timer, label = Timer(lambda: heap_sort(arr.tolist())), 'heapsort'
print(timer.timeit(1),label)

timer, label = Timer(lambda: merge_sort(arr.tolist())), 'merge_sort'
print(timer.timeit(1),label)