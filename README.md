# Explorable-Heap-Selection using Randomised Heap Exploration

An implementation and application of the algorithm from the IPCO 2023 paper "A Nearly Optimal Randomized Algorithm for Explorable Heap Selection."

The algorithm efficiently finds the nth smallest element in an infinitely large binary heap with traversal-based access, achieving an expected time complexity of $O(n \log^3 (n))$ using $O(\log n)$ space.

We implement the algorithm and use it for a branch and bound approach for 0-1 knapsack modelled as an integer linear programming problem.

## Applications

The algorithm is particularly useful for the branch-and-bound optimization method which is often used in integer linear programming. We demonstrate this use in our code.

## How to run

1. Install necessary libraries:

```bash
pip install networkx pulp
```

2. Go into src/ folder

3. To test the base algorithm, write the following in the terminal:

```bash
python3 RandomisedHeapExploration.py
```

4. To test the application for branch and bound optimization on knapsack, write the following in the terminal:

```bash
python3 BranchNBound.py
```

Other uses:

- Run the base algorithm for larger n by modifying the value of n in the file `src/RandomisedHeapExploration.py`

- Visualise the base algorithm for small n (< 10) by setting `visualise=True` in the file `src/RandomisedHeapExploration.py`. THe animation will be saved in the root folder as `heap_animation.mp4`

- Run the branch and bound optimization on a different knapsack problem by changing `data_option = "Small"` in the file `src/BranchNBound.py`

## Implementation Details

## Code Structure

## Time Analysis Plots

## Memory Usage Plots

## Sample Run

# Paper Link

[A Nearly Optimal Randomized Algorithm for Explorable Heap Selection](https://doi.org/10.1007/978-3-031-32726-1_3)
