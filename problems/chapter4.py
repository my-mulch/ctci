
def path_exists(a,b):
    a.visited = True
    queue = [a]

    while queue:
        current = queue.pop(0)
        
        if current is b:
            return True
        
        for node in current.adjacent:
            if not node.visited:
                node.visited = True
                queue.append(node)
    
    return False
