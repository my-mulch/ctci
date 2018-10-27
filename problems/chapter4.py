
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
