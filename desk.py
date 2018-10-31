from problems import chapter8
import numpy as np

A, B, C = [1,
           2,
           3,
           4,
           5,
           6,
           7,
           8], [], []

chapter8.towers_of_hanoi(disks=len(A), source=A, buffer=C, target=B)

print(A, B, C)
