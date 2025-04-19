import Heap
import math 
def selectN(n: int, T: Heap):
	k = 1
	curr = T.head
	L = curr.val	
	while k < n:
		if k < n /2:
			alt_k = 2 * k
		else: 
			alt_k = n
		L = extend(T, alt_k, k, L)
		k = alt_k
	return L



