import numpy as np
matrix = np.matrix([[1, 2, -1], [3, 4, 1], [5, 1, -3]])
vector = np.matrix([[-3], [1], [-2]])
x = ([[0], [0], [0]])

def JG(matrix, vector):
    x = (matrix**(-1)*vector)
    print(x)
JG(matrix, vector)