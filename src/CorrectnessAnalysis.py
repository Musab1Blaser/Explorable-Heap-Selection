from baseline.BestFirst import best_first
import heap.Heap as Heap
from RandomisedHeapExploration import selectN
from heap.NodeValGenerator import randGen
import random


tally = 0
print("First 5 samples:")
total = 50
for i in range(total):
    n = random.randint(100, 50000) # size from 100 to 500000
    nheap = Heap.Heap(randGen)
    
    ans1 = selectN(nheap, n)
    ans2 = best_first(nheap, n)
    
    if i < 5:
        print("Elements:", n)
        print("Our answer:", ans1)
        print("Expected answer:", ans2)
        print()
    
    if ans1 == ans2:
        tally += 1
        
    if (i+1) % 10 == 0:
        print(f"Processed {i+1}/{total}")
print(f"Correct results: {tally}/{total}")
        