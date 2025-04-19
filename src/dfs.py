import Heap
from Heap import Node 

def dfsHelper(root: Node, L:float, n, count = 0  ):
	curr = root
	if curr != None:
		if curr.val > L:
			return 0
		if curr.val == L:
			return 1
		if count == n:
			return -1
		left = 0
		left = dfsHelper(curr.getLeft, L, n, count +1)
		if left == -1:
			return -1
		right = 0
		right = dfsHelper(curr.getRight, L,n, count + left + 1)
		if right == -1:
			return -1
		return left + right + 1
	else:
		return 0
	
def dfs(T: Heap, L:float, n):
	""" 
	DFS function to find the number of elements in the heap that are less than or equal to L
	"""
	count = dfsHelper(T.head, L, n)
	if count == -1:
		return n + 1
	return count