import numpy as np
import math
x = np.array([1.5, 2, 2.5, 3, 3.5], dtype = float)
y = np.array([10.517, 10.193, 9.807, 9.387, 8.977], dtype = float)
y1 = np.array([0, 0, 0, 0], dtype = float)
y2 = np.array([0, 0, 0], dtype = float)
y3 = np.array([0, 0], dtype = float)
y4 = np.array([0], dtype = float)
e = 0.001
x1 = 1.684
x2 = 5.756
q1 = 0
q2 = 0
b1 = 0
b2 = 0
qtemp = 0
i = 0
h = x[1] - x[0]
q1 = abs(x1 - x[0])
while i<len(x):
    if q1 < abs(x1 - x[i]):
        q1 = q1
    else:
        q1 = abs(x1 - x[i])
        b1 = i
    i = i + 1
i = 0

q2 = abs(x2 - x[0])
while i<len(x):
    if q2 < abs(x2 - x[i]):
        q2 = q2
    else:
        q2 = abs(x2 - x[i])
        b2 = i
    i = i + 1

print("x[",b1,"]; ", "q1: ", q1, " ", "x[",b2,"]; " "q2: ", q2)

i = len(y) - 1
while i >= 1:
    y1[i-1] = abs(y[i] - y[i-1])
    i = i - 1

i = len(y1) - 1
while i >= 1:
    y2[i-1] = abs(y1[i] - y1[i-1])
    i = i - 1

i = len(y2) - 1
while i >= 1:
    y3[i-1] = abs(y2[i] - y2[i-1])
    i = i - 1

i = len(y3) - 1
while i >= 1:
    y4[i-1] = abs(y3[i] - y3[i-1])
    i = i - 1

f1 = y[b1] + q1*y1[b1] + y2[b1]*(q1*(q1-1)/math.factorial(2)) + y3[b1]*(q1*(q1-1)*(q1-2)/math.factorial(3)) + y4[b1]*(q1*(q1-1)*(q1-2)*(q1-3)/math.factorial(4))
print("f1: ", f1)

f2 = 0 + q2*0 + 0*(q2*(q2-1)/math.factorial(2)) + 0*(q2*(q2-1)*(q2-2)/math.factorial(3)) + 0*(q2*(q2-1)*(q2-2)*(q2-3)/math.factorial(4))
print("f2: ", f2)

deriv11 = (1/h)*(y1[b1] + y2[b1]*((2*q1-1)/2) + y3[b1]*((3*(q1**2)-6*q1+2)/2) + y4[b1]*((2*(q1**3)-9*(q1**2)+11*q1-3)/12))
print("deriv11: ", round(deriv11, 3))

deriv21 = (1/h)*(0 + 0*((2*q2-1)/2) + 0*((3*(q2**2)-6*q2+2)/2) + 0*((2*(q2**3)-9*(q2**2)+11*q2-3)/12))
print("deriv21: ", round(deriv21, 3))

deriv12 = (1/(h**2))*(y2[b1] + y3[b1]*(q1-1) + y4[b1]*((6*(q1**2)-18*q1+11)/12))
print("deriv12: ", round(deriv12, 3))

deriv22 = (1/(h**2))*(0 + 0*(q2-1) + 0*((6*(q2**2)-18*q2+11)/12))
print("deriv22: ", round(deriv22, 3))