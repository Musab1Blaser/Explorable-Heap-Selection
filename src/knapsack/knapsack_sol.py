# SOURCE: https://slama.dev/youtube/linear-programming-in-python/

from pulp import *


# three datasets (small/medium/large)
# each contains weights / prices / knapsack carry weight
data = {
        "Small": [   
            [12, 7, 11, 8, 9],
            [24, 13, 23, 15, 16],
            26,
        ],
        
        "Medium": [
            [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
            165,
        ]
}

def knap_solve(problem_sz):
    weights, prices, carry_weight = data[problem_sz]
    n = len(weights)

    model = LpProblem(sense=LpMaximize)

    # variables - binary based on if we take the item or not
    variables = [LpVariable(name=f"x_{i}", cat=LpBinary) for i in range(n)]

    # inequalities - don't exceed the carry weight
    model += lpDot(weights, variables) <= carry_weight

    # objective function - price of the items we take
    model += lpDot(prices, variables)

    _ = model.solve(PULP_CBC_CMD(msg=False))

    # print(problem_sz + " - " + str(n) + "\n" + "-" * len(problem_sz))
    print("Price:", model.objective.value())
    print("Select:", [int(variables[i].value()) for i in range(n)])
    print()