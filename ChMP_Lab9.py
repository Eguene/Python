import numpy as np
import math
import matplotlib.pyplot as plt
x = np.array([0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23])
y = np.array([5.5154, 5.4669, 5.3263, 5.1930, 5.0664, 4.9461, 4.8317, 4.7226, 4.6185, 4.5191, 4.4242])
x1 = 0.184
x2 = 0.221
h = x[1] - x[0]
q1 = (x1 - x[0])/h
q2 = (x2 - x[9])/h
y1 = np.array([None]*10)
y2 = np.array([None]*9)
y3 = np.array([None]*8)
y4 = np.array([None]*7)
y5 = np.array([None]*6)
y6 = np.array([None]*5)
y7 = np.array([None]*4)
y8 = np.array([None]*3)
y9 = np.array([None]*2)
y10 = np.array([None]*1)
i = 0
while i < len(y)-1:
    y1[i] = y[i+1] - y[i]
    i = i + 1
print("y1: ", y1)

i = 0
while i < len(y1)-1:
    y2[i] = y1[i+1] - y1[i]
    i = i + 1
print("y2: ", y2)

i = 0
while i < len(y2)-1:
    y3[i] = y2[i+1] - y2[i]
    i = i + 1
print("y3: ", y3)

i = 0
while i < len(y3)-1:
    y4[i] = y3[i+1] - y3[i]
    i = i + 1
print("y4: ", y4)

i = 0
while i < len(y4)-1:
    y5[i] = y4[i+1] - y4[i]
    i = i + 1
print("y5: ", y5)

i = 0
while i < len(y5)-1:
    y6[i] = y5[i+1] - y5[i]
    i = i + 1
print("y6: ", y6)

i = 0
while i < len(y6)-1:
    y7[i] = y6[i+1] - y6[i]
    i = i + 1
print("y7: ", y7)

i = 0
while i < len(y7)-1:
    y8[i] = y7[i+1] - y7[i]
    i = i + 1
print("y8: ", y8)

i = 0
while i < len(y8)-1:
    y9[i] = y8[i+1] - y8[i]
    i = i + 1
print("y9: ", y9)

i = 0
while i < len(y9)-1:
    y10[i] = y9[i+1] - y9[i]
    i = i + 1
print("y10: ", y10)

NeutonForm1 = y[0] + q1*y1[0] + ((q1*(q1 - 1))/math.factorial(2))*y2[0] + ((q1*(q1 - 1)*(q1 - 2))/math.factorial(3))*y3[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3))/math.factorial(4))*y4[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3)*(q1 - 4))/math.factorial(5))*y5[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3)*(q1 - 4)*(q1 - 5))/math.factorial(6))*y6[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3)*(q1 - 4)*(q1 - 5)*(q1 - 6))/math.factorial(7))*y7[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3)*(q1 - 4)*(q1 - 5)*(q1 - 6)*(q1 - 7))/math.factorial(8))*y8[0] + ((q1*(q1 - 1)*(q1 - 2)*(q1 - 3)*(q1 - 4)*(q1 - 5)*(q1 - 6)*(q1 - 7)*(q1 - 8))/math.factorial(9))*y9[0]
print(NeutonForm1)
NeutonForm2 = y[9] + q2*y1[8] + ((q2*(q2 + 1))/math.factorial(2))*y2[7] + ((q2*(q2 + 1)*(q2 + 2))/math.factorial(3))*y3[6] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3))/math.factorial(4))*y4[5] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3)*(q2 + 4))/math.factorial(5))*y5[4] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3)*(q2 + 4)*(q1 + 5))/math.factorial(6))*y6[3] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3)*(q2 + 4)*(q1 + 5)*(q1 + 6))/math.factorial(7))*y7[2] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3)*(q2 + 4)*(q2 + 5)*(q2 + 6)*(q2 + 7))/math.factorial(8))*y8[1] + ((q2*(q2 + 1)*(q2 + 2)*(q2 + 3)*(q2 + 4)*(q2 + 5)*(q2 + 6)*(q2 + 7)*(q2 + 8))/math.factorial(9))*y9[0]
print(NeutonForm2)

linspx = np.linspace(0.18, 0.23, 200)
linspy = np.linspace(NeutonForm1, NeutonForm2, 200)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolate function")
plt.plot(linspx, linspy, 'g-')
plt.grid()
plt.show()