from NodeValGenerator import *
import networkx as nx
import matplotlib.pyplot as plt

"""
Heap:
    Attributes:
        - head (Type: Node)
        
Node:
    Attributes:
        - val (Type: Float)
        - restrictions (Type: List of {0, 1}) - only used for Knapsack
        - terminal (Type: Boolean) = only used for Knapsack
        
        - color (Type: String) - only used for visualisation
        - __left (Type: Node) [PRIVATE]
        - __right (Type: Node) [PRIVATE]
        
    Methods:
        getLeft(): Returns left child (Creates it if it doesn't exist)
        getRight(): Returns right child (Creates it if it doesn't exist)
        
generationStrategy:
    Specifies how nodes are created
    - firstN: Heap is effectively a flat array of [1,2,3, ..., n]
    - randGen: Heap contains random positive floats rounded to 1 decimal place
    - knapsack: Heap contains value as per Linear Programming with restrictions
"""

color_options = [
    "red", "orange", "yellow", "green",
    "violet", "pink", "cyan", "lime"
]


class Node():
    def __init__(self, val, restrictions=None, terminal=False):
        self.val = val
        
        # for knapsack
        self.restrictions = restrictions
        self.terminal = terminal
        
        # Children will be initialised on access
        self.__left = None
        self.__right = None
        
    def __lt__(self, other):
        return self.val < other.val
    
    def __repr__(self):
        return str(self.val)
    
    def __str__(self):
        return str(self.val)
        
    def getLeft(self):
        if not self.__left:
            self.__left = Node(*generationStrategy(self, 0))
        return self.__left
    
    def getRight(self):
        if not self.__right:
            self.__right = Node(*generationStrategy(self, 1))
        return self.__right

class Heap():
    def __init__(self, strategy, head = None):
        global generationStrategy
        generationStrategy = strategy
        if head != None:
            self.head = head
        else:
            self.head = Node(*generationStrategy(None, 0))
             
# Tests:
# def printHeapBFS(head, depth):
#     frontier = [head]
#     while depth > 0:
#         newFrontier = []
#         for node in frontier:
#             print(node.val, end=" ")
#             newFrontier.append(node.getLeft())
#             newFrontier.append(node.getRight())
#         print()
#         frontier = newFrontier
#         depth -= 1

def drawHeap(head, depth):
    G = nx.DiGraph()
    pos = {}
    id = 0

    # add root
    G.add_node(id, label=str(head.val), color=color_options[depth])
    pos[id] = (0, 0)
    frontier = [(id, head)] # id, node and x pos
    id += 1
    depth -= 1
    
    # go through each level
    dx = 1024
    dy = -100
    while depth > 0:
        newFrontier = []
        for node in frontier:
            # left node
            G.add_node(id, label=str(node[1].getLeft().val), color=color_options[depth])
            G.add_edge(node[0], id)
            pos[id] = (pos[node[0]][0] - dx, pos[node[0]][1] + dy) # left of parent (-dx), and below (+dy)
            newFrontier.append((id, node[1].getLeft()))
            id += 1
            
            # right node
            G.add_node(id, label=str(node[1].getRight().val), color=color_options[depth])
            G.add_edge(node[0], id)
            pos[id] = (pos[node[0]][0] + dx, pos[node[0]][1] + dy) # right of parent (-dx), and below (+dy)
            newFrontier.append((id, node[1].getRight()))
            id += 1
        
        depth -= 1 # next level
        frontier = newFrontier
        dx = dx//2 # to prevent nodes from different subtrees overlapping
        
    labels = nx.get_node_attributes(G, 'label')
    colors = [G.nodes[i].get('color', 'gray') for i in G.nodes]
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels = labels, node_size=1000, node_color=colors)
    plt.show()

    
if __name__ == "__main__":
    nheap = Heap(firstN)
    # printHeapBFS(nheap.head, 4)
    drawHeap(nheap.head, 5)        
        