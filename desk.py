from problems import chapter3
import numpy as np


queue = chapter3.StackQueue()

queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.enqueue('d')
queue.enqueue('e')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.enqueue('f')
queue.enqueue('g')
queue.enqueue('h')
queue.enqueue('i')

print(queue.dequeue())
print(queue.dequeue())

queue.enqueue('j')
queue.enqueue('k')
queue.enqueue('l')
queue.enqueue('m')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
