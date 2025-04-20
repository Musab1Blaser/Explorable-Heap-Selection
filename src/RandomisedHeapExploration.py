import heap.Heap as Heap
import math

from subroutines.dfs import dfs
from subroutines.goodValues import goodValues
from subroutines.root import roots 
from heap.NodeValGenerator import *
from baseline.BestFirst import best_first

# exact implementation of extend
def extend(T: Heap.Heap , TreeHead: Heap.Node, n, k , L_0):
	Heap.color_idx += 1
	# print("Diving in")
	L = L_0
	U = math.inf
	while k < n:
		r = roots(TreeHead, L_0, L, U)
		L_alt = max(L, r.val) 
		k_alt = dfs(TreeHead, L_alt, n)
		c = dfs(r, L_alt, n)
		c_alt = min(n-k_alt+c, 2*c)
		while k_alt < n:
			L_alt = extend(T, r, c_alt, c, L_alt)
			k_alt = dfs(TreeHead, L_alt, n)
			c = c_alt
			c_alt = min(n-k_alt+c, 2*c)
		L_hat, U_hat = goodValues(T, TreeHead, r, L_alt, n)
		L = max(L, L_hat)
		U = min(U, U_hat)
		k = dfs(TreeHead, L, n, recolor=True)
	# print("Jumping out")
	Heap.color_idx -= 1
	return L 


# exact implementation of selectN
def selectN(T: Heap.Heap, n: int):
	k = 1
	curr = T.head
	L = curr.val	
	while k < n:
		if k < n /2:
			alt_k = 2 * k
		else: 
			alt_k = n
		L = extend(T, curr, alt_k, k, L)
		k = alt_k
	return L


if __name__ == "__main__":
    visualise = True # set True if you wish to generate the animation - will take more memory and time !! ONLY DO WITH SMALL VALUES OF N (e.g. < 10) !!
    n = 8 # specify n -> which value of heap to find
    print(f"Searching for the {n}-th smallest value")
    
    nheap = Heap.Heap(firstN, visualise=visualise) # first parameter is heap type: firstN, randGen
    
    ans = selectN(nheap, n) # run algorithm
    if visualise:
        nheap.save_animation() # generates visualisation
    
    print("Randomised Heap Exploration result:", ans)
    print("Expected answer (by Best First):", best_first(nheap, n))
    
    if n <= 10: # displays small heaps for further analysis
        Heap.drawHeap(nheap.head, 5)
