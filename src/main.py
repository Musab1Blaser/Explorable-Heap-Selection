import Heap
import math

from dfs import dfs
from goodValues import goodValues
from root import roots 
from NodeValGenerator import *
from BestFirst import best_first

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
    visualise = False
    nheap = Heap.Heap(randGen, visualise=visualise)
    n = 10
    # printHeapBFS(nheap.head, 4)
    ans = selectN(nheap, n)
    if visualise:
        nheap.save_animation()
    print("Our answer:", ans)
    print("Expected answer:", best_first(nheap, n))
    Heap.drawHeap(nheap.head, 5)
