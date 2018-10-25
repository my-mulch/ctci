from problems import chapter2
from tools.structures.link import LinkedList

a = LinkedList(node_variety='double')

a.insert(10, 'tail')
a.insert(9, 'tail')
a.insert(1, 'tail')
a.insert(1, 'tail')
a.insert(9, 'tail')
a.insert(10, 'tail')


print(chapter2.is_palindrome(a))
