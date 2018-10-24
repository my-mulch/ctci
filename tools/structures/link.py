from node.link_node import LinkNode

class LinkedList():

    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def __str__(self):

        def callback(node):
            callback.state += "- |  {}  | -".format(node.data)
        
        callback.state = ''
        callback.done = False

        return self.traverse(callback)

    def traverse(self, fn):
        runner = self.head
        
        while(runner):
            fn(runner)
            
            if fn.done:
                break

            runner = runner.next
        
        return fn.state

    def delete(self, data):
        def callback(node):
            if node.data == data:
                callback.done = True

                if node.prev and node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                elif node.prev is None: # trying to delete head
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None

                else: # trying to delete tail
                    self.tail = self.tail.prev
                    if self.tail:
                        self.tail.next = None
        
        callback.state = ''
        callback.done = False
        
        self.traverse(callback)


    def insert(self, node, insertion_point):
        if type(node) is not LinkNode:
            node = LinkNode(node)

        if getattr(self, insertion_point) is None:
            self.head = node
            self.tail = node
            return
        
        point_new = 'prev' if insertion_point == 'head' else 'next'
        point_old = 'next' if point_new == 'prev' else 'prev'
        
        insertion_node = getattr(self, insertion_point)

        setattr(insertion_node, point_new, node)
        setattr(node, point_old, insertion_node)
        setattr(self, insertion_point, node)
        
    

dll = LinkedList()

dll.insert(10, 'tail')
dll.insert(17, 'tail')
dll.insert(13, 'head')

dll.delete(13)
dll.delete(17)
dll.delete(10)

dll.insert(11, 'head')
dll.insert(47, 'head')
dll.insert(22, 'head')
dll.insert(22, 'tail')

print(dll)





