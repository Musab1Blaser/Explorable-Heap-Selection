## Problem
### Branch and Bound
Linear programming. Trying to optimize a quantity. Make small changes to values of \textbf{x}. Easy to make change in one element then in many elements, hence idea of spatial locality

### Explorable Heap
Maybe binary search on possible target values to find best value for linear system


## Solution
### Key ideas
DFS(T, v, n) -> For a given value, dfs can be used to identify whether it is <= SELECT n in O(n) time <br>
We keep estimates of how small SELECT n can be and how large, for e.g. initially small is value of root and large is infinity. Once we start crossing n nodes explored, then large can start being bounded by the smallest value we have seen above bounds <br>
Finding n-th largest value is essentially finding first n values. Idea here is find first 1, 2, 4, 8, ..., n values. By exploring further and further out. We consider good subtrees (so their leaves are bounded). Then we explore the subtrees rooted at those leaves and continue. <br>
Idea for random sampling is quite creative. Keeps $O(1)$ memory.
