from problems import chapter2
from tools.structures.link import LinkedList

dll = LinkedList(node_variety='double')

dll.insert(9, 'tail')
dll.insert(3, 'tail')
dll.insert(8, 'tail')
dll.insert(3, 'tail')
dll.insert(1, 'tail')
dll.insert(3, 'tail')
dll.insert(6, 'tail')
dll.insert(3, 'tail')
dll.insert(4, 'tail')
dll.insert(7, 'tail')

print(dll)

chapter2.partition(dll, 4)

print(dll)