from Heap import Node
import Heap

r = None

def rootHelper(root: Node, L_0: float, L: float, U: float):
	global r
	"""
	Roots function to find the element, r, in T for which the value is greater than L_0, and its subtree has an element >L and less than U.
	"""
	# returns -1 if no such element is found
	if root is None:
		return -1
	#go deep if value is smaller than L_0
	if root.val < L_0:
		left = rootHelper(root.getLeft(), L_0, L, U)
		if left != None:
			return left
		right = rootHelper(root.getRight(), L_0, L, U)
		return right
	else:
		# if this is the first node which is greater than L_0 then save it and go deeper
		if r == None:
			r = rootHelper(r, L_0, L, U)
			return r
		# if the value exceeds U then the r is not to be returned
		if root.val > U:
			return None
		# if the value is less than U and greater than R then r is to be returned
		elif root.val > L:
			return r
		#go deeper otherwise into each of their subtrees.
		left = rootHelper(root.getLeft, L_0, L, U)
		#return if  the value required is found
		if left != None:
			return left
		right = rootHelper(root.getRight, L_0, L, U)
		#no subtrees left so just return whatever the value of this subtree is
		return right
	


def root(T: Heap, L_0: float, L: float, U: float):
	return rootHelper(T.head, L_0, L, U)
	