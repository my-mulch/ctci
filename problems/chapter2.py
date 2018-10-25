
def delete_dups(linked_list):
    runner = linked_list.head
    seen = set()
    
    while(runner):
        if runner.data in seen:
            if runner.next:
                runner.next.prev = runner.prev
            
            runner.prev.next = runner.next
        else:
            seen.add(runner.data)
        
        runner = runner.next
    
    return linked_list


def kth_to_last(linked_list, k):
    r1 = linked_list.head
    r2 = linked_list.head
    
    for i in range(k):
        r1 = r1.next
    
    while(r1):
        r1 = r1.next
        r2 = r2.next
    
    return r2


def delete_mid_node(mid_node):
    next_node = mid_node.next
    mid_node.data = next_node.data
    mid_node.next = next_node.next

def partition(linked_list, p):
    runner = linked_list.head
    
    while(runner):
        if runner.data < p:
            linked_list.insert(runner.data, 'head')

            if runner.prev:	
                runner.prev.next = runner.next
            if runner.next:
                runner.next.prev = runner.prev
        
        runner = runner.next


