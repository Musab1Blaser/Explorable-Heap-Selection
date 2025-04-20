from heap.NodeValGenerator import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

"""
Heap:
    Attributes:
        - head (Type: Node) -> head of heap
        
        for knapsack:
        - terminal_node (Type: Node) -> completely restricted/terminal node -> integer solution
        - terminal_val (Type: int) -> value of integer solution
        
        for animation:
        - visualise_flag (Type: Bool) -> whether or not to create animation
        
    Methods:
        - save_animation(): compile graph G history to create animation
    
Node:
    Attributes:
        - val (Type: Float)
        - __left (Type: Node) [PRIVATE]
        - __right (Type: Node) [PRIVATE]
        
        for knapsack:
        - restrictions (Type: List of {0, 1}) - which items have to be taken/not taken
        - terminal (Type: Boolean) - is an integer solution
        
        for animation:
        - id (Type: int) - used to identify node in Networkx Graph 
        - color (Type: String) - to control color of node
        
    Methods:
        - getLeft(): Returns left child (Creates it if it doesn't exist)
        - getRight(): Returns right child (Creates it if it doesn't exist)
        
        for animation:
        - changeColor(): Update color of node for animation
        
generationStrategy:
    Specifies how nodes are created
    - firstN: Heap is effectively a flat array of [1,2,3, ..., n]
    - randGen: Heap contains random positive floats rounded to 1 decimal place
    - knapsack_selector("Small" | "Medium"): Heap contains value as per Linear Programming with restrictions
"""

# For animation:
color_options = [
    "pink", "violet", "lime",
    "red", "orange", "yellow", "green"
]

color_idx = -1
animation_frames = []
visualise_flag = False
G = nx.DiGraph()
pos = {}
dx = {}
dy = -100
id = 0

def capture_frame():
    global animation_frames, G, pos

    # Make deep copies so future updates don't mutate past frames
    frame_G = copy.deepcopy(G)
    frame_pos = copy.deepcopy(pos)
    
    animation_frames.append((frame_G, frame_pos))

# ------------------------------------------------------------------- #
class Node():
    def __init__(self, val, restrictions=None, terminal=False):
        global id
        self.id = id
        id += 1
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
        global G, visualise_flag, pos, dx, dy, color_options, color_idx
        if not self.__left:
            self.__left = Node(*generationStrategy(self, 0))
            if visualise_flag:
                G.add_node(self.__left.id, label=str(self.__left.val), color=color_options[color_idx])
                G.add_edge(self.id, self.__left.id)
                pos[self.__left.id] = (pos[self.id][0] - dx[self.id], pos[self.id][1] + dy)
                dx[self.__left.id] = dx[self.id]//2
                G.nodes[self.__left.id]['color'] = color_options[color_idx]
                capture_frame()
        return self.__left
    
    def getRight(self):
        global G, visualise_flag, pos, dx, dy, color_options, color_idx
        if not self.__right:
            self.__right = Node(*generationStrategy(self, 1))
            if visualise_flag:
                G.add_node(self.__right.id, label=str(self.__right.val), color=color_options[color_idx])
                G.add_edge(self.id, self.__right.id)
                pos[self.__right.id] = (pos[self.id][0] + dx[self.id], pos[self.id][1] + dy)
                dx[self.__right.id] = dx[self.id]//2
                G.nodes[self.__right.id]['color'] = color_options[color_idx]
                capture_frame()
        return self.__right
    
    def changeColor(self, color=""):
        global G, visualise_flag, color_options
        if visualise_flag:
            prev_color = G.nodes[self.id]['color']
            if color:
                G.nodes[self.id]['color'] = color
            else:
                G.nodes[self.id]['color'] = color_options[color_idx] 
            if prev_color != G.nodes[self.id]['color']:
                capture_frame()

class Heap():
    def __init__(self, strategy, visualise=False):
        global generationStrategy, G, pos, id, color_idx, color_options, visualise_flag
        generationStrategy = strategy
        self.head = Node(*generationStrategy(None, 0))

        self.terminal_val = 0
        self.terminal_node = None
        
        visualise_flag = visualise
        if visualise_flag:
            G.add_node(self.head.id, label=str(self.head.val), color=color_options[color_idx + 1])
            pos[self.head.id] = (0, 0)
            dx[self.head.id] = 1024
            capture_frame()
            
    def save_animation(self):
        global animation_frames
        fig, ax = plt.subplots(figsize=(12, 8))

        def draw_frame(i):
            ax.clear()
            frame_G, frame_pos = animation_frames[i]

            labels = nx.get_node_attributes(frame_G, 'label')
            colors = [frame_G.nodes[n].get('color', 'gray') for n in frame_G.nodes]

            nx.draw_networkx_nodes(frame_G, frame_pos, ax=ax, node_color=colors, node_size=1000)
            nx.draw_networkx_edges(frame_G, frame_pos, ax=ax)
            nx.draw_networkx_labels(frame_G, frame_pos, labels=labels, ax=ax)
            ax.set_title(f"Frame {i}")

        if visualise_flag and animation_frames:
            ani = animation.FuncAnimation(
                fig,
                draw_frame,
                frames=len(animation_frames),
                interval=500,
                blit=False  # turn off blitting to avoid redraw issues with text
            )
            ani.save("../heap_animation.mp4", writer='ffmpeg')
            plt.close(fig)

# ------------------------------------------------------------------- #

def drawHeap(head, depth): # draw first few levels of heap
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
        