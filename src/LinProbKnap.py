from pulp import *

data = {
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
}

def linprobknap(restrictions, problem="Medium"):
    model = LpProblem(sense=LpMinimize) # since storing value as negative, want minimum
    weights, prices, capacity  = data[problem]
    n = len(weights)
    variables = [LpVariable(name=f"x_{i}", lowBound=0, upBound=1) for i in range(n)]
    
    for i in range(len(restrictions)): # fixed value
        model += variables[i] == restrictions[i]
        # model += variables[i] >= restrictions[i]
        
    model += lpDot(weights, variables) <= capacity
    model += lpDot(prices, variables)
    
    model.solve(PULP_CBC_CMD(msg=False))
    val = model.objective.value()
    terminal = True
    for variable in variables:
        if variable.value() // 1 != variable.value():
            terminal = False
            
    if val > 0:
        return 0, False
    # print(val, terminal)
    return val, terminal

# print(linprobknap([1, 1, 1, 1, 0, 1, 0, 0, 0, 0]))