import heap.Heap as Heap
from heap.NodeValGenerator import knapsack_selector
from baseline.BestFirst import best_first
from RandomisedHeapExploration import selectN
from knapsack.knapsack_sol import knap_solve

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
    data_option = "Medium" # "Small" or "Medium"
    print("Problem instance:", data_option)
    nheap = Heap.Heap(knapsack_selector(data_option))
    
    lim = 1 # we double this until we reach a terminal node
    while True:
        _ = selectN(nheap, lim)
        if nheap.terminal_node:
            ans, rest = find_best(nheap.head, nheap.terminal_val)
            print("Branch and Bound via Explorable Heap results for knapsack:")
            print("Value:", -ans) # answer is negative since we were using a minheap to solve a maximisation problem
            print("Select:", rest)
            print()
            break
        lim *= 2
        
    print("Expected result by baseline ILP solver:")
    knap_solve(data_option)