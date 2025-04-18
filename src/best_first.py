import Heap
import heapq

def best_first(head, n):
    lst = [] # first n elements
    pq = []
    heapq.heappush(pq, head)
    while len(lst) < n:
        cur = heapq.heappop(pq)
        lst.append(cur)
        heapq.heappush(pq, cur.getLeft())
        heapq.heappush(pq, cur.getRight())
        
    print(lst)
    
if __name__ == "__main__":
    nheap = Heap.Heap()
    # printHeapBFS(nheap.head, 4)
    best_first(nheap.head, 8)        
    Heap.drawHeap(nheap.head, 5)


