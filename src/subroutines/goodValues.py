import random
import heap.Heap as Heap
import math

from subroutines.dfs import dfs

rand_node = None
count = 0


def SSampler(r, L, U):
    global rand_node, count
    if r.val < U:
        SSampler(r.getLeft(), L, U)
        SSampler(r.getRight(), L, U)
    if r.val > L and r.val < U:
        count += 1
        if random.random() < 1 / count: # swap given a probability -> allows for chance of candidate = 1/num_candidates
            rand_node = r

def goodValues(T: Heap.Heap, TreeHead: Heap.Node, T_r: Heap.Node, alt_L: float, n:int):
	global rand_node, count
	L = -math.inf
	if dfs(TreeHead, alt_L, n, T) != n + 1: # is good
		L = alt_L
	# otherwise it is bad and we can let U = alt_L
	U = alt_L
 
	# while cardinality of S' is greater than 0
	while True:
		# sample randomly
		rand_node = None
		count = 0
		SSampler(T_r, L, U)
		if rand_node is None:
			break

		dfsVal = dfs(TreeHead, rand_node.val, n, T)
		if  dfsVal!= n+1: # is good
			L = rand_node.val
		else: # is bad
			U = rand_node.val
   
	# final condition, if L = L' = U then make U inf
	if L == alt_L and alt_L == U:
		U = math.inf
	return L, U

