from problems import chapter17
import numpy as np

n = 15

nums = [i for i in range(n)]
np.random.shuffle(nums)

missing_index = np.random.randint(n)
missing_value = nums[missing_index]
del nums[missing_index]

assert(missing_value == chapter17.find_missing(nums))
