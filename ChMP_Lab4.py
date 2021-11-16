import numpy as np
import random

def randNum(a, b):
    x=random.randint(a, b)
    return x

print('завдання 1 номер 3')
a = np.matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
b = np.matrix([[7, 5, 3], [0, 7, 5], [0, 0, 7]])
print('AB - BA = ', (a*b)-(b*a))
print('завдання 2 номер 2')
c = np.matrix([[-1, 0, 0], [0, 1, 0], [1, 2, -1]])
d = np.linalg.matrix_power(c, 2)
print('C^2 = ', d)
print('завдання 3 номер 4')
a = np.matrix([[5, 0, 2, 3], [4, 1, 5, 3], [3, 1, -1, 2]])
b = np.matrix([[6], [-2], [7], [4]])
print('A*B = ', a*b)
print('завдання 4 номер 4')
a = np.matrix('1 2 3; -1 2 1; 1 3 2')
det_a=np.linalg.det(a)
print('det a=',det_a)
print('завдання 5 номер 3')
a = np.matrix('1 2 0 0 0; 1 0 2 0 0; 1 0 0 2 0; 1 0 0 0 2; 0 0 1 1 1')
det_a=np.linalg.det(a)
print('det a=',det_a)
print('завдання 6 номер 4')
a = np.matrix([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
b = np.linalg.matrix_rank(a)
print('Rank = ', b)
print('завдання 7 номер 3')
a = np.matrix([[-2, 3, 1, -1], [3, 2, 1, 4], [1, 2, 3, 4], [0, 2, 3, 3]])
b = np.linalg.matrix_rank(a)
print('Rank = ', b)
print('завдання 8 номер 4')
a = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
b = np.matrix([[-1], [5], [28]])
c = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
d = np.linalg.matrix_power(a, -1)
c[0, 0] =  -1
c[1, 0] =  5
c[2, 0] =  28
det_a=np.linalg.det(c*d)
print ('x = ', det_a)
c = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
c[0, 1] =  -1
c[1, 1] =  5
c[2, 1] =  28
det_b=np.linalg.det(c*d)
print ('y = ', det_b)
c = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
c[0, 2] =  -1
c[1, 2] =  5
c[2, 2] =  28
det_c=np.linalg.det(c*d)
print ('z = ', det_c)
print('завдання 9 номер 4')
a = np.matrix([[2, -1, 1], [3, 4, -2], [1, -3, 1]])
b = np.matrix([[5], [-3], [4]])
c = np.linalg.solve(a, b)
print(c)
print('завдання 10 номер 4')
N = int(input()) ##строки
M = int(input()) ##столбцы
matrix = list()
for i in range(N):
    strings = list()
    for j in range(M):
        strings.append(randNum(1, 5))
    matrix.append(strings)
for i in range(N):
    for j in range(M):
            print(matrix[i][j], end=' ')
    print()
msum = 0
partmsum = 0
for i in range(N):
    for j in range(M):
        msum = msum + matrix[i][j]
print(msum)
for j in range(M):
    for i in range(N):
        partmsum = partmsum + matrix[i][j]
    print(partmsum)
    print((partmsum/msum)*100,"%")
    partmsum = 0