from problems import chapter3
import numpy as np

stack = chapter3.MegaStack()

nums = np.random.randint(0,10,1000)

for num in nums:
    getattr(stack, 'pop' if np.random.rand() < 0.5 else 'push')(num)
    print(stack.stacks)
