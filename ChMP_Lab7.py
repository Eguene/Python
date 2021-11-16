import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
x1 = np.array([-1, 0, 1, 2], dtype = float)
x2 = np.array([-0.5, 0.5, 1.5, 2.5], dtype = float)
y1 = np.array([-20, -5, 6, 25], dtype = float)
y2 = np.array([0, 0, 0, 0], dtype = float)
e = 0.001
def Lagr(x1, x2, y1, y2):
	i = 0
	while i<len(x2):
		y2[i] = ((((x2[i] - x1[1])*(x2[i] - x1[2])*(x2[i] - x1[3]))/((x1[0] - x1[1])*(x1[0] - x1[2])*(x1[0] - x1[3])))*y1[0]) + ((((x2[i] - x1[0])*(x2[i] - x1[2])*(x2[i] - x1[3]))/((x1[1] - x1[0])*(x1[1] - x1[2])*(x1[1] - x1[3])))*y1[1]) + ((((x2[i] - x1[0])*(x2[i] - x1[1])*(x2[i] - x1[3]))/((x1[2] - x1[0])*(x1[2] - x1[1])*(x1[2] - x1[3])))*y1[2]) + ((((x2[i] - x1[0])*(x2[i] - x1[1])*(x2[i] - x1[2]))/((x1[3] - x1[0])*(x1[3] - x1[1])*(x1[3] - x1[2])))*y1[3])
		print("F(x[",i,"]) = ", y2[i])
		i+=1
	print(y2)
	i = 0
	plt.plot(x2, y2, "ko-", label ="Lagrange")
	plt.show()
Lagr(x1, x2, y1, y2)
print("Check: ", lagrange(x2, y2))