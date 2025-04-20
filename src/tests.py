from subroutines.dfs import dfs
from heap.NodeValGenerator import *
from baseline.BestFirst import best_first
import heap.Heap as Heap
import math
from RandomisedHeapExploration import selectN
import time
import numpy as np
import matplotlib.pyplot as plt

timeWithRandGen = []
timeWithBestFirst = []
n_values = [10**exp for exp in range(1, 7)]
for n in n_values:  # Powers from 10^1 to 10^6
	visualise = False
	# nheap = Heap.Heap(randGen, visualise=visualise)
	nheap = Heap.Heap(firstN, visualise=visualise)
	print(f"Testing with n = {n}")
	startTime =time.time()
	ans = selectN(nheap, n)
	endTime = time.time()
	if visualise:
		nheap.save_animation()
	timeWithRandGen.append(endTime - startTime)
	
	print("Our answer:", ans)
	startTime =time.time()
	print("Expected answer:", best_first(nheap, n))
	endTime =time.time()
	timeWithBestFirst.append(endTime - startTime)
	print("-" * 50)

	

# Create x-axis values (powers of 10)


# Create the plot

# Calculate timeWithRandGen divided by n*(log(n))^3

# plt.plot(n_values, timeWithRandGen, 'o-', label='Randomised Heap Exploration')
# plt.plot(n_values, timeWithBestFirst, 's-', label='Best First')

# # Set logarithmic scale for x-axis
# plt.xscale('log')
# plt.yscale('log')

# # Add labels and title
# plt.xlabel('n (log scale)')
# plt.ylabel('Time (seconds, log scale)')
# plt.title('Performance Comparison: Randomised Heap Exploration vs Best First using randGen initialisation')
# plt.legend()
# plt.grid(True, which="both", ls="--")

# # Add x-tick labels

# # Show the plot
# plt.tight_layout()
# plt.savefig('performance_comparison.png')
# plt.show()

plt.figure(figsize=(10, 6))
plt.xticks(n_values, [f'10^{exp}' for exp in range(1, 7)])
normalized_time = [t / (n * (math.log(n, 2)**3)) for t, n in zip(timeWithRandGen, n_values)]
plt.plot(n_values, normalized_time, 'o-', label='Randomised Heap Exploration (normalized by n*(log n)^3)')
normalized_time = [t / (n * (math.log(n, 2)**2)) for t, n in zip(timeWithRandGen, n_values)]
plt.plot(n_values, normalized_time, 'o-', label='Randomised Heap Exploration (normalized by n*(log n)^2)')
normalized_time = [t / (n * (math.log(n, 2))) for t, n in zip(timeWithRandGen, n_values)]
plt.plot(n_values, normalized_time, 'o-', label='Randomised Heap Exploration (normalized by nlog(n))')
normalized_time = [t / n  for t, n in zip(timeWithRandGen, n_values)]
plt.plot(n_values, normalized_time, 'o-', label='Randomised Heap Exploration (normalized by n)')

# Set logarithmic scale for x-axis
plt.xscale('log')
plt.yscale('log')

plt.xlabel('n (log scale)')
plt.ylabel('Time (seconds, log scale)')
plt.title('Normalised time taken by Randomised Heap Exploration')
plt.legend()
plt.grid(True, which="both", ls="--")
# Show the plot
plt.tight_layout()
plt.savefig('normalised_performance_comparison.png')
plt.show()
