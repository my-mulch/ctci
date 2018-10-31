from problems import chapter8, chapter1
import numpy as np

arr = sorted(np.random.randint(0, 50, 21).tolist())

chapter1.binary_search(arr, 100)
