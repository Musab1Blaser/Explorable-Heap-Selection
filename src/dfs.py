import Heap

lCount = 0

def dfsHelper(root: Heap.Node, L:float, n, count = 0, T:Heap.Heap = None, recolor=False): # to allow for duplicate elements, we need count to return num elements, and return -1 if more than n elements less than L
	global lCount	
	curr = root
	if T and curr.terminal and curr.val < T.terminal_val:
		T.terminal_node = curr
		T.terminal_val = curr.val
  
	if curr.val > L:
		curr.changeColor("black")
		return 0
	else:
		curr.changeColor()
  
	if curr.val == L:
		lCount += 1
	count += 1
	if count - max(0, lCount-1) > n: # can ignore lcount-1 of nodes == L -> report if still exceeding limit
		return -1

	left = 0
	left = dfsHelper(curr.getLeft(), L, n, count, T)
	if left == -1:
		return -1
	count += left
 
	right = 0
	right = dfsHelper(curr.getRight(), L, n, count, T)
	if right == -1:
		return -1
	count += right
 
	return 1 + left + right # only returns what was in its subtree
	
def dfs(TreeHead: Heap.Node, L:float, n, T:Heap.Heap = None, recolor = False):
	""" 
	DFS function to find the number of elements in the heap that are less than or equal to L
	"""
	global lCount
	lCount = 0
	count = dfsHelper(TreeHead, L, n, 0, T, recolor=True)
	if count == -1:
		return n+1
	else:
		return min(count, n)