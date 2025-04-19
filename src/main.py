import Heap
import math

import dfs
import goodValues
from root import root 


# exact implementation of extend
def extend(T: Heap, n, k , L_0):
	L = L_0
	U = math.inf
	while k < n:
		r = root(T, L_0, L, U)
		L_alt = max(L, r.val)
		k_alt = dfs(T, L_alt, n)
		c = dfs(Heap(r), L_alt, n)
		c_alt = min(n-k_alt+c, 2*c)
		while k_alt < n:
			L_alt = extend(Heap(r), c_alt, c, L_alt)
			k_alt = dfs(T, L_alt, n)
			c = c_alt
			c_alt = min(n-k_alt+c, 2*c)
		L_hat, U_hat = goodValues(T, r, L_alt, n)
		L = min(L, L_hat)
		U = min(U, U_hat)
		k = dfs(T, L, n)
	return L 


# exact implementation of selectN
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



