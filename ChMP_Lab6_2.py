from scipy import optimize
def fun(x):
    return [x[1] + math.cos(x[0]) - 1.5, 2*x[0] - math.sin(x[1] - 0.5) - 1]
    sol = optimize.root(fun, [0, 0], method='hybr')
    print(sol.x)
