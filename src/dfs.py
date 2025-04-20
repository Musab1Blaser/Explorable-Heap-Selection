import Heap

lCount = 0

def dfsHelper(root: Heap.Node, L:float, n, count = 0): # to allow for duplicate elements, we need count to return num elements, and return -1 if more than n elements less than L
	global lCount	
	curr = root
	if curr.val > L:
		return 0
	if curr.val == L:
		lCount += 1
	count += 1
	if count - max(0, lCount-1) > n: # can ignore lcount-1 of nodes == L -> report if still exceeding limit
		return -1

	left = 0
	left = dfsHelper(curr.getLeft(), L, n, count)
	if left == -1:
		return -1
	count += left
 
	right = 0
	right = dfsHelper(curr.getRight(), L, n, count)
	if right == -1:
		return -1
	count += right
 
	return 1 + left + right
	
def dfs(TreeHead: Heap.Node, L:float, n):
	""" 
	DFS function to find the number of elements in the heap that are less than or equal to L
	"""
	global lCount
	lCount = 0
	count = dfsHelper(TreeHead, L, n)
	if count == -1:
		return n+1
	else:
		return min(count, n)