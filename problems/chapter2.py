
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


def sum_lists(a, b, sum_list):
    a_runner = a.tail
    b_runner = b.tail
    
    carry = 0
    while(a_runner or b_runner):
        sum_digit = 0
        
        if a_runner:
            sum_digit += a_runner.data
            a_runner = a_runner.prev
        
        if b_runner:
            sum_digit += b_runner.data
            b_runner = b_runner.prev
        
        sum_digit += carry
        new_digit = sum_digit % 10
        carry = 1 if sum_digit > 9 else 0
        sum_list.insert(new_digit, 'head')
        
    if carry:
        sum_list.insert(carry, 'head')
            
    return sum_list

def is_palindrome(linked_list):
    twox_runner = linked_list.head
    head_runner = linked_list.head
    tail_runner = linked_list.tail

    while twox_runner:
        twox_runner = twox_runner.next
        
        if twox_runner: # prevents that runoff the edge shiet
            twox_runner = twox_runner.next

        if head_runner.data != tail_runner.data:
            return False
        
        head_runner = head_runner.next
        tail_runner = tail_runner.prev
    
    return True

def intersect(a,b):
    a_runner = a.head
    b_runner = b.head

    stack_a = []
    stack_b = []
    
    while a_runner:
        stack_a.append(a_runner)
        a_runner = a_runner.next

    while(b_runner):
        stack_b.append(b_runner)
        b_runner = b_runner.next
    
    if stack_a[-1] is not stack_b[-1]:
        return None
    
    a_last = None
    b_last = None
    previous = None

    while(a_last is b_last):
        previous = a_last
        a_last = stack_a.pop()
        b_last = stack_b.pop()

    return previous

