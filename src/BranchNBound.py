import Heap
from NodeValGenerator import knapsack, firstN
from BestFirst import best_first

def find_best(head, lim):
    stack = [head]
    ans = 0
    ans_rest = []
    while len(stack):
        newStack = []
        for cur in stack:
            if len(cur.restrictions) == 10:
                if cur.val < ans:
                    ans = cur.val
                    ans_rest = cur.restrictions
            else: 
                x = cur.getLeft()
                if x.val <= lim: 
                    newStack.append(x)
                    
                x = cur.getRight()
                if x.val <= lim: 
                    newStack.append(x)
        stack = newStack
    return ans, ans_rest
            
            
        
if __name__ == "__main__":
    lim = 1
    nheap = Heap.Heap(knapsack)
    while True:
        node = best_first(nheap.head, lim)
        print(node, node.terminal)
        print(node.restrictions)
        if node.terminal:
            print(find_best(nheap.head, node.val))
            break
        lim *= 2