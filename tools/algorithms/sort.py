from ..misc import swap
from ..structures.heap import Heap

def heap_sort(arr):
    heap = Heap(arr)
    Heap.build_max_heap(heap)
    
    while heap.size:
        heap.extract_max()

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left=merge_sort(arr[:len(arr)//2])
    right=merge_sort(arr[len(arr)//2:])
    
    return merge(left,right)

def merge(left,right):
    merged = []
    lt = rt = 0

    while lt < len(left) and rt < len(right):
        if left[lt] <= right[rt]:
            merged.append(left[lt])
            lt+=1
        else:
            merged.append(right[rt])
            rt+=1
    
    merged.extend(right[rt:]) if rt < len(right) else merged.extend(left[lt:])

    return merged
    

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j-1, j)
            j-=1


def insertion_sort_bin(arr):
    for i in range(1, len(arr)):
        
        # on average 20 % faster than regular see bench.py
        e=i-1
        s=0
     
        while(s <= e):
            m = (e+s) // 2
            if arr[i] <= arr[m]:
                e = m - 1
            else:
                s = m + 1
        
        j=i
        while j > s:
            swap(arr, j-1, j)
            j-=1
        



