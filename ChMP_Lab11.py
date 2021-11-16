import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
def func(x):
    return math.sin(math.cos(x))
def derivFirst(x):
    return (-1)*(math.sin(x))*math.cos(math.cos(x))
def derivSecond(x):
    return (-1)*(math.sin(x)**2)*math.sin(math.cos(x)) - math.cos(x)*math.cos(math.cos(x))
def derivThird(x):
    return (math.sin(x)**3)*math.cos(math.cos(x)) - 3*math.sin(x)*math.sin(math.cos(x))*math.cos(x) + math.sin(x)*math.cos(math.cos(x))
def derivFourth(x):
    return (math.sin(x)**4)*math.sin(math.cos(x)) + 4*(math.sin(x)**2)*math.sin(math.cos(x)) + 6*(math.sin(x)**2)*math.cos(x)*math.cos(math.cos(x)) - 3*math.sin(math.cos(x))*(math.cos(x)**2) + math.cos(x)*math.cos(math.cos(x))
def f1(x):
    return func(x) + derivFirst(x)*(x - 0) + derivSecond(x)*((x - 0)**2)/math.factorial(2) 
def f2(x):
    return func(x) + derivFirst(x)*(x - 0) + derivSecond(x)*((x - 0)**2)/2 + derivThird(x)*((x - 0)**3)/math.factorial(3)

print("derivFourth(1): ", derivFourth(1))
print("derivFourth(0): ", derivFourth(0))
print("derivFourth(-1): ", derivFourth(-1))

if derivFourth(1) > derivFourth(-1):
    n = derivFourth(1)
elif derivFourth(-1) > derivFourth(1):
    n = derivFourth(-1)
else:
    n = derivFourth(1)

if derivFourth(0) > n:
    n = derivFourth(0)
else: 
    n = derivFourth(1)

m = math.ceil(n)
print("m = ", m)

R3 = (m/math.factorial(3))*abs((((2**5)/5) - ((1**5)/5)))
print("R3 = ", R3)

x1 = np.linspace(-1, 1, 100)
y1 = np.linspace(func(0), func(1), 100)
y2 = np.linspace(f2(0), f2(1), 100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Taylor polynomial")
plt.plot(x1, y1, 'g-', x1, y2, 'r-')
plt.grid()
plt.show()