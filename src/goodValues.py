import random
import Heap
from Heap import Node
import math
import bisect

from dfs import dfsHelper



def makeS(root: Node, alt_L: float, s: list):
	curr = root
	if curr.val > alt_L:
		return 
	bisect.insort_left(s, curr.val)
	makeS(curr.getLeft, alt_L, s)
	makeS(curr.getRight, alt_L, s)

	


def goodValues(T: Heap, T_r: Node, alt_L: float, n:int):
	L = -math.inf
	U = math.inf
	s = []
	# get the set S we are to analyse
	makeS(T_r, alt_L, s)
	# start of the item init max
	L_ind = 0
	#end of the items init min
	U_ind = len(s) - 1

	# while cardinality of S' is greater than 0
	while U_ind > L_ind :
		# sample randomly
		index = random.randint(L_ind, U_ind - L_ind)
		if dfsHelper(T_r, s[index], n) < n:
			L = s[index]
			L_ind = index
		else: 
			U = s[index]
			U_ind = index
	# final condition, if L = L' = U then make U inf
	if L == alt_L and alt_L == U:
		U = math.inf
	return L, U

