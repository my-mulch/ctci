from tools.algorithms.sort import insertion_sort, insertion_sort_bin, heap_sort

import numpy as np
import time

arr = np.random.randint(0,20,20000)

start_time = time.time()
insertion_sort_bin(arr.tolist())
end_time = time.time()

print(end_time - start_time, "seconds for", "insertion-bin")

start_time = time.time()
insertion_sort(arr.tolist())
end_time = time.time()

print(end_time - start_time, "seconds for", "insertion-reg")

start_time = time.time()
heap_sort(arr.tolist())
end_time = time.time()

print(end_time - start_time, "seconds for", "heap")
