
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
    length=0
    runner=linked_list.head
    while(runner):
        length+=1
        runner=runner.next
    
    runner=linked_list.head
    while(length>k):
        length-=1
        runner=runner.next
    
    return runner