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

kth_to_last = chapter2.kth_to_last(dll, 3)

print(kth_to_last.data)