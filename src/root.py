import Heap
import random

r = None
count = 0

def checkSubtree(r: Heap.Node, L_0: float, L: float, U: float):
    if r.val > L and r.val < U: # if in range, then we are done
        return True
    elif r.val < U: # if not in range but less than U, means also less than L_0 -> we must explore further
        return checkSubtree(r.getLeft(), L_0, L, U) or checkSubtree(r.getRight(), L_0, L, U)
    else: # at least equal to U means subtree wont be in range so we can stop here
        return False

def rootPicker(root : Heap.Node, L_0, L, U):
	global r, count
    
    #go deep if value is smaller than L_0
	if root.val <= L_0: 
		rootPicker(root.getLeft(), L_0, L, U) # will update r by itself
		rootPicker(root.getRight(), L_0, L, U) # will update r by itself
  
	else: # if > L_0 for the first time -> mark node if feasible (has some child in range)
		if checkSubtree(root, L_0, L, U):
			count += 1
			# root.changeColor("lightblue")
			if random.random() < 1/count:
				if r:
					r.changeColor("lightblue")
				root.changeColor("cyan")
				r = root

def roots(root: Heap.Node, L_0: float, L: float, U: float):
	"""
	Roots function to randomly sample an element, r, in T for which the value is greater than L_0, and its subtree has an element > L and < U.
	"""

	global r, count
	r = None
	count = 0
	rootPicker(root, L_0, L, U)
	return r