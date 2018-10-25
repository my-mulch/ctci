from problems import chapter2
from tools.structures.link import LinkedList

a = LinkedList(node_variety='double')

a1 = a.insert(10, 'tail')
a2 = a.insert(9, 'tail')
a3 = a.insert(18980, 'tail')
a4 = a.insert(1, 'tail')
a5 = a.insert(9, 'tail')
a6 = a.insert(10, 'tail')

b = LinkedList(node_variety='double')
b1 = b.insert(2, 'tail')
b2 = b.insert(5, 'tail')
b3 = b.insert(3, 'tail')
b4 = b.insert(4, 'tail')
b5 = b.insert(a3, 'tail')


print(chapter2.intersect(a,b).data)
