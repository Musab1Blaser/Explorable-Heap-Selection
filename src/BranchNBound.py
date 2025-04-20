import Heap
from NodeValGenerator import knapsack, firstN
from BestFirst import best_first
from main import selectN

def find_best(head, lim): # explore up till the limit to find the highest value terminal node
    stack = [head]
    ans = 0
    ans_rest = []
    while len(stack):
        newStack = []
        for cur in stack:
            if cur.terminal: # may be a terminal node
                if len(cur.restrictions) > len(ans_rest) or cur.val < ans: # save best value and solution
                    ans = cur.val
                    ans_rest = cur.restrictions
            # explore further if best value may be part of subtree
            x = cur.getLeft()
            if x.val <= lim: 
                newStack.append(x)
                
            x = cur.getRight()
            if x.val <= lim: 
                newStack.append(x)
        stack = newStack
    return ans, ans_rest
            
            
        
if __name__ == "__main__":
    lim = 1 # we double this until we reach a terminal node
    nheap = Heap.Heap(knapsack)
    while True:
        # node = best_first(nheap, lim)
        _ = selectN(nheap, lim)
        # print(node, node.terminal)
        # print(node.restrictions)
        if nheap.terminal_node:
            ans, rest = find_best(nheap.head, nheap.terminal_val)
            print(-ans) # answer is negative since we were using a minheap to solve a maximisation problem
            print(rest)
            break
        lim *= 2