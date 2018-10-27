from .base_node import BaseNode


class DoubleLinkNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.next = None
        self.prev = None


class SingleLinkNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.next = None


class LinkedList():

    def __init__(self, data=None, node_variety='single'):

        self.node_variety = SingleLinkNode if node_variety == 'single' else DoubleLinkNode

        self.head = None if data is None else self.node_variety(data)
        self.tail = None if data is None else self.node_variety(data)

    def __str__(self):
        link_symbol = '=' if self.node_variety is DoubleLinkNode else '-'

        def callback(previous, node):
            callback.state += "{1} |  {0}  | {1}".format(
                node.data, link_symbol)

        callback.state = ''
        callback.done = False

        return self.traverse(callback)

    def traverse(self, fn):
        runner = self.head
        previous = self.head

        while(runner):
            fn(previous, runner)

            if fn.done:
                break

            previous = runner
            runner = runner.next

        return fn.state

    def delete(self, data):
        def callback(previous, node):
            if node.data == data:
                callback.done = True

                if self.node_variety == DoubleLinkNode:
                    if node.prev and node.next:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                    else:
                        location = 'head' if self.head is node else 'tail'
                        pointnew = 'next' if self.head is node else 'prev'
                        pointold = 'prev' if self.head is node else 'next'

                        end_node = getattr(self, location)
                        new_node = getattr(end_node, pointnew)
                        setattr(self, location, new_node)

                        if new_node:
                            setattr(new_node, pointold, None)

                elif self.node_variety == SingleLinkNode:
                    if node is self.head:
                        self.head = self.head.next

                        if self.head is None:
                            self.tail = None

                    elif node is self.tail:
                        self.tail = previous
                        self.tail.next = None

                    else:
                        previous.next = node.next

        callback.state = ''
        callback.done = False

        self.traverse(callback)

    def insert(self, node, insertion_point):
        if type(node) is not self.node_variety:
            node = self.node_variety(node)

        if getattr(self, insertion_point) is None:
            self.head = node
            self.tail = node
            return node

        if self.node_variety == DoubleLinkNode:
            point_new = 'prev' if insertion_point == 'head' else 'next'
            point_old = 'next' if insertion_point == 'head' else 'prev'

            insertion_node = getattr(self, insertion_point)

            setattr(insertion_node, point_new, node)
            setattr(node, point_old, insertion_node)

        elif self.node_variety == SingleLinkNode:
            point_new = 'next'
            insertion_node = node if insertion_point == 'head' else self.tail
            insertion_dest = node if insertion_point == 'tail' else self.head

            setattr(insertion_node, point_new, insertion_dest)

        setattr(self, insertion_point, node)
        return node
