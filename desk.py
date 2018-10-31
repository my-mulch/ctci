from problems import chapter8
import numpy as np

power_set = chapter8.power_set([1, 2, 3, 4, 5])
print(len(power_set))

for s in power_set:
    print(s)
