from .base_node import BaseNode


class BinaryTreeNode(BaseNode):
    def __init__(self, data):
        super().__init__(data)

        self.left = None
        self.right = None
        self.parent = None


class BinaryTree():

    def __init__(self, tree=[]):
        tree[0] = tree[0] if type(
            tree[0]) is BinaryTreeNode else BinaryTreeNode(tree[0])
        
        self.root = tree[0]

        if not len(tree) % 2:
            tree.append(None)

        for i in range(len(tree) // 2):
            node = tree[i]

            for c in range(1, 3):  # 2 children in binary tree
                child_index = 2 * i + c
                child_pointer = 'left' if c == 1 else 'right'

                if tree[child_index] is not None:
                    
                    tree[child_index] = tree[child_index] if type(
                        tree[child_index]) is BinaryTreeNode else BinaryTreeNode(tree[child_index])

                    setattr(node, child_pointer, tree[child_index])
                    setattr(getattr(node, child_pointer), 'parent', node)


examples = [BinaryTree([6, 4, 8, 3, 5, 7, 9])]
