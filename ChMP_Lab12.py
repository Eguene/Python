import math
import numpy as np
import matplotlib.pyplot as plt
xarray = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
yarray = []
xx = 0
yy = 0
xx2 = 0
yx = 0
a1 = 0
a0 = 0
i = 0

while i < len(xarray):
    yarray.append(math.sin(math.cos(xarray[i])))
    i +=1
i = 0

while i < (len(xarray)-1):
    xx += xarray[i]
    yy += yarray[i]
    xx2 += (xarray[i])**2
    yx += xarray[i]*yarray[i]
    i += 1

xx = xx/len(xarray)
yy = yy/len(xarray)
xx2 = xx2/len(xarray)
yx = yx/len(xarray)
a1 = (yx - xx*yy)/(xx2 - xx**2)
a0 = yy - a1*xx

print("x average = ", xx) 
print("x**2 = ", xx2)
print("y average = ", yy) 
print("yx = ", yx) 
print("a1 = ", a1)
print("a0 = ", a0)

def funcline(xarray):
    f = a0 + a1*xarray
    return f

xs = np.array(np.linspace(0, 1))
f = np.vectorize(funcline)

plt.plot(xarray, yarray, 'ro', xs, f(xs), 'g-')
plt.axis([0, 1, 0, 3])
plt.scatter(xarray, yarray)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()