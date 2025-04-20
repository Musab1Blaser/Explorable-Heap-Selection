import random
from knapsack.LinProbKnap import linprobknap

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

def knapsack_selector(problem_size): # problem size: "Small" or "Medium"
    lims = {"Small" : 5, "Medium" : 10}
    def knapsack(node, off): # Heap contains value as per Linear Programming with restrictions
        if node is None:
            restrictions = [] # root node has no restrictions
        else:
            restrictions = node.restrictions[:]
            if len(restrictions) < lims[problem_size]: # add restrictions to children
                restrictions += [off]
            else:
                return 1, restrictions, False # so that I no longer consider this subtree
            
        val, term = linprobknap(restrictions, problem=problem_size)
        return val, restrictions, term
    return knapsack
    

     
     

