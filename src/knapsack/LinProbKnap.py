# Derived from: https://slama.dev/youtube/linear-programming-in-python/

from pulp import *

data = { # we make values negative so that the problem becomes a minimization problem
    "Small": [
        [12, 7, 11, 8, 9],
        [-i for i in [24, 13, 23, 15, 16]],
        26
        ],
   
    "Medium":[
        [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        [-i for i in [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]],
        165
        ],
    
    "Large":[
        [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684],
        [-i for i in [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261]],
        6404180,
    ]
}

def linprobknap(restrictions, problem): # Solves linear programming problem (not Integer Linear Programming) with restrictions
    model = LpProblem(sense=LpMinimize) # since storing value as negative, want minimum
    weights, prices, capacity  = data[problem]
    n = len(weights)
    variables = [LpVariable(name=f"x_{i}", lowBound=0, upBound=1) for i in range(n)]
    
    for i in range(len(restrictions)): # fixed value
        model += variables[i] == restrictions[i]
        
    model += lpDot(weights, variables) <= capacity
    model += lpDot(prices, variables)
    
    model.solve(PULP_CBC_CMD(msg=False))
    
    val = model.objective.value() # value of solution
    terminal = True # is node an integer solution
    for variable in variables:
        if variable.value() // 1 != variable.value():
            terminal = False
            
    if val > 0 or sum(weights[i]*variables[i].value() for i in range(n)) > capacity: # correct invalid solutions -> potentially occur due to numerical instability
        return 1, False
    return val, terminal
