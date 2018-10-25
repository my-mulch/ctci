from problems import chapter2
from tools.structures.link import LinkedList

a = LinkedList(node_variety='double')

a.insert(9, 'tail')
a.insert(9, 'tail')
a.insert(9, 'tail')
a.insert(1, 'tail')

b = LinkedList(node_variety='double')

b.insert(1, 'tail')
b.insert(0, 'tail')
b.insert(9, 'tail')

sum = LinkedList(node_variety='double')

chapter2.sum_lists(a,b,sum)
print(sum)