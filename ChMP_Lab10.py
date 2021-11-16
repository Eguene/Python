import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = array([0.3, 0.5, 0.8, 1.2, 1.7], dtype = float)
y = array([2.38, 2.94, 1.46, 1.28, 2.15], dtype = float)
spl = UnivariateSpline(x, y)
xs = linspace(0.3, 1.7, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.grid(color = 'b',
         linestyle = '-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline')
plt.show()