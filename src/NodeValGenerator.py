import random
from LinProbKnap import linprobknap

def firstN(node, off):
    if node is None:
        return 1.0
    else:
        return 2*node + off, None

def randGen(node, off):
    if node is None:
        val = 0
    else:
        val = node.val
    return round(val + 0.1 + random.random()*10, 1), None

def knapsack(node, off):
    if node is None:
        restrictions = []
    else:
        restrictions = node.restrictions[:]
        if len(restrictions) < 10:
            restrictions += [off]
    
    val, term = linprobknap(restrictions)
    return val, restrictions, term
     
     

