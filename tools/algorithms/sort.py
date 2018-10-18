from ..misc import swap
from ..structures.heap import Heap

def heap_sort(arr):
    heap = Heap(arr)
    Heap.build_max_heap(heap)
    
    while heap.size:
        heap.extract_max()


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j-1, j)
            j-=1


def insertion_sort_bin(arr):
    for i in range(1, len(arr)):
        
        # on average 14 % faster than regular see bench.py
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
        



