from pulp import *
    
def knapsack(weights, prices, capacity):
    model = LpProblem("Task 2", LpMaximize)
    n = len(weights)
    variables = [LpVariable(name = f"x_{i}", cat = LpBinary) for i in range(n)]

    # lpDot(coefficients, variables)
    model += lpDot(prices, variables)
    model += lpDot(weights, variables) <= capacity

    status = model.solve()
    print("Task 2 results:")
    print("Status:", LpStatus[status])
    for i in range(n):
        print(f"x_{i} =", variables[i].value())
    return


def chromatic(vertices, edges):
    n = len(vertices)
    variables = [[LpVariable(name = f"x_{u}_{k}", cat = LpBinary) for k in range(n)] for u in range(n)]
    chromatic = LpVariable("chromatic_num", lowBound = 0, upBound = n, cat = "Integer")

    model = LpProblem("Task 3", LpMinimize)
    model += chromatic

    for u in range(n):
        model += lpSum(variables[u]) == 1

    for e in edges:
        for k in range(n):
            model += variables[e[0]][k] + variables[e[1]][k] <= 1

    for u in range(n):
        for k in range(n):
            model += (k+1)*variables[u][k] <= chromatic

    status = model.solve()
    print("Task 3 results:")
    print("Status:", LpStatus[status])
    for u in range(n):
        for k in range(n):
            print(f"x_{u}_{k} =", variables[u][k].value())
    return
    

def main():
    # -------------------------------------------------
    # EXAMPLE
    print("Example")
    # Maximization model
    model = LpProblem("Example", LpMaximize)

    # Variables
    x = LpVariable("x", lowBound=0, cat="Integer")
    y = LpVariable("y", lowBound=0, cat="Integer")

    # Objective function
    model += 3 * x + 2 * y

    # Constraints
    model += 2.5 * x + y <= 100
    model += x + y <= 80

    # Solve problem (CBC solver)
    status = model.solve()

    # Show result
    print("Results:")
    print("Status:", LpStatus[status])
    print("x =", x.value())
    print("y =", y.value())

    # -------------------------------------------------
    # Task 4b
    print("\n-----------------------------------------\n")
    print("Task 4b")
    model2 = LpProblem("Task 4b", LpMinimize)

    y1 = LpVariable("y1", lowBound=0, cat = "Continuous")  
    y2 = LpVariable("y2", lowBound=0, cat="Continuous")

    model2 += 8*y1 + 4*y2

    model2 += y1 + y2 >= 2
    model2 += y1 - y2 >= 1

    status = model2.solve()

    print("Task 4b results:")
    print("Status:", LpStatus[status])
    print("x =", y1.value())
    print("y =", y2.value())

    # -------------------------------------------------
    # Task 1
    print("\n-----------------------------------------\n")
    print("Task 1")

    model3 = LpProblem("Task 1", LpMinimize)

    x1 = LpVariable("x1", lowBound = 0, cat = "Continuous")
    x2 = LpVariable("x2", lowBound = 0, cat = "Continuous")
    x3 = LpVariable("x3", lowBound = 0, cat = "Continuous")

    model3 += 40*x1 + 100*x2 + 150*x3

    model3 += x1 + 2*x2 + 2*x3 == 3
    model3 += 30*x1 + 10*x2 + 20*x3 == 75

    status = model3.solve()

    print("Task 1 results:")
    print("Status:", LpStatus[status])
    print("x1 =", x1.value())
    print("x2 =", x2.value())
    print("x3 =", x3.value())

    # -------------------------------------------------
    # Task 2
    # Knapsack problem
    print("\n-----------------------------------------\n")
    print("Task 2")

    weights = [12, 7, 11, 8, 9]
    prices =  [24, 13, 23, 15, 16]
    capacity = 26

    # weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    # prices = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    # capacity = 165

    # weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959,
    # 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951,
    # 264724, 224916, 169684]
    # prices = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693,
    # 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027,
    # 65731, 901489, 577243, 466257, 369261]
    # capacity = 6404180

    knapsack(weights, prices, capacity)

    # -------------------------------------------------
    # Task 3
    print("\n-----------------------------------------\n")
    print("Task 3")

    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (0, 4), (1, 4), (0, 3), (0, 2)]

    # vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # edges = [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9), (5, 7),
    #  (5, 8), (6, 8), (6, 9), (7, 9)]

    # vertices = [0, 1, 2, 3, 4, 5]
    # edges = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 5)]

    chromatic(vertices, edges)

if __name__ == "__main__":
    main()