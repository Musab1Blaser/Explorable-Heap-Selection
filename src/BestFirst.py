import Heap
import heapq
from NodeValGenerator import *

def best_first(Heap : Heap.Heap, n): # ignores the travel constraint - finds nth largest node
    head = Heap.head
    lst = [] # first n elements
    pq = [] # next nodes to explore/active nodes
    heapq.heappush(pq, head)
    
    while len(lst) < n: # expand smallest active node
        cur = heapq.heappop(pq)
        if cur.terminal and cur.val < Heap.terminal_val:
            Heap.terminal_node = cur
            Heap.terminal_val = cur.val

        lst.append(cur)
        heapq.heappush(pq, cur.getLeft())
        heapq.heappush(pq, cur.getRight())
        
    return lst[-1].val
    
if __name__ == "__main__":
    nheap = Heap.Heap(firstN)
    # printHeapBFS(nheap.head, 4)
    ans = best_first(nheap, 8)
    print(ans)
    Heap.drawHeap(nheap.head, 5)