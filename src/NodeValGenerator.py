import random
from LinProbKnap import linprobknap

def firstN(node, off): # Heap is effectively a flat array of [1,2,3, ..., n]
    if node is None:
        return 1.0,
    else:
        return 2*node.val + off,

def randGen(node, off): # Heap contains random positive floats rounded to 1 decimal place
    if node is None:
        val = 0
    else:
        val = node.val
    return round(val + 0.1 + random.random()*10, 1),

def knapsack(node, off): # Heap contains value as per Linear Programming with restrictions
    data_option = "Medium" # "Small" or "Medium"
    lims = {"Small" : 5, "Medium" : 10}
    
    if node is None:
        restrictions = [] # root node has no restrictions
    else:
        restrictions = node.restrictions[:]
        if len(restrictions) < lims[data_option]: # add restrictions to children
            restrictions += [off]
        else:
            return random.random(), restrictions, False # so that I no longer consider this subtree
        
    val, term = linprobknap(restrictions, problem=data_option)
    return val, restrictions, term
     
     

