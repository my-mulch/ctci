from problems import chapter2
from tools.structures.link import LinkedList

dll = LinkedList(node_variety='single')

dll.insert(10, 'tail')
dll.insert(17, 'tail')

mid = dll.insert(11, 'tail')

dll.insert(17, 'tail')
dll.insert(22, 'tail')
dll.insert(22, 'tail')

print(dll)

chapter2.delete_mid_node(mid)

print(dll)