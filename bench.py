from tools.algorithms.sort import insertion_sort, insertion_sort_bin, heap_sort, merge_sort

import numpy as np
from timeit import Timer

arr = np.random.randint(0, 20, 10000).tolist()

print(Timer(lambda: insertion_sort(arr)).timeit(1), 'insertion-reg')
print(Timer(lambda: insertion_sort_bin(arr)).timeit(1), 'insertion-bin')
print(Timer(lambda: heap_sort(arr)).timeit(1), 'heapsort')
print(Timer(lambda: merge_sort(arr)).timeit(1), 'merge_sort')
