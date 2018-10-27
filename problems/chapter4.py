import math


def path_exists(graph, a, b, verbose=False):
    a.visited = True
    queue = [a]

    while queue:
        current = queue.pop(0)

        if verbose:
            print('----------', current.data, '----------')

        if current is b:
            return True

        for i in current.adjacent:
            node = graph.nodes[i]

            if not node.visited:

                if verbose:
                    print(node.data)

                node.visited = True
                queue.append(node)

    return False


def minimal_tree(arr, low, high):
    mid = (high + low) // 2

    if high < low:
        return

    print(arr[mid])
    minimal_tree(arr, low, mid - 1)
    minimal_tree(arr, mid + 1, high)


def level_lists(binary_tree):
    my_level_lists = {}

    for i, node in enumerate(binary_tree):
        level = math.floor(math.log(i + 1, 2))

        if level not in my_level_lists:
            my_level_lists[level] = []

        my_level_lists[level].append(node)

    return my_level_lists


def check_balance(root):
    if not root:
        return -1

    left_height = check_balance(root.left)
    if left_height == 'error':
        return 'error'
    left_height += 1

    right_height = check_balance(root.right)
    if right_height == 'error':
        return 'error'
    right_height += 1

    if abs(left_height - right_height) > 1:
        return 'error'

    return left_height + right_height


def validate_bst(root, prev=[None]):
    if not root:
        return True

    if not validate_bst(root.left, prev):
        return False

    if prev[0] and prev[0].data > root.data:
        return False

    prev[0] = root

    if not validate_bst(root.right, prev):
        return False

    return True


def successor(node, level=0):
    if not node:
        return None

    if not level:
        if node.right:
            return successor(node.right, level + 1)
        else:
            
    else:
        left = successor(node.left, level + 1)
        
        if left is not None:
            return left

        return node
        successor(node.right, level + 1)
