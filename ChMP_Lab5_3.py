## а тут даже все работает, и вроде правильно. Тоже не без костылей, но они незначительные. Опять таки, не забудь поудалять все мои комменты.
import numpy as np
matrix = np.matrix([[1, 2, -1], [3, 4, 1], [5, 1, -3]])
vector = np.matrix([[-3], [1], [-2]])
x = ([[0], [0], [0]])

def mainelchoose(matrix, vector):
    n = len(vector) - 1
    x[n] = vector[n]/matrix[n, n]
    i = n - 1
    while i >= 1:
        j = i + 1
        summ = 0
        while j <= n:
            summ = summ + matrix[i, j] * x[j]
            j+=1
        x[i] = (vector[i] - summ)/matrix[i, i]
        print(x[i])
        i=i-1
mainelchoose(matrix, vector)