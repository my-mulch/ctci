from problems import chapter2
from tools.structures.link import LinkedList

dll = LinkedList()

dll.insert(10, 'tail')
dll.insert(17, 'tail')
dll.insert(11, 'head')
dll.insert(11, 'head')
dll.insert(17, 'head')
dll.insert(22, 'head')
dll.insert(22, 'tail')

print(dll)

chapter2.delete_dups(dll)

print(dll)
