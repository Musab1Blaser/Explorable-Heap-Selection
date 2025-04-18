import Heap
import heapq
from NodeValGenerator import *

def best_first(head, n):
    lst = [] # first n elements
    pq = []
    heapq.heappush(pq, head)
    while len(lst) < n:
        cur = heapq.heappop(pq)
        lst.append(cur)
        heapq.heappush(pq, cur.getLeft())
        heapq.heappush(pq, cur.getRight())
        
    # print(lst)
    return lst[-1]
    
if __name__ == "__main__":
    nheap = Heap.Heap(randGen)
    # printHeapBFS(nheap.head, 4)
    ans = best_first(nheap.head, 8)
    print(ans)        
    Heap.drawHeap(nheap.head, 5)


