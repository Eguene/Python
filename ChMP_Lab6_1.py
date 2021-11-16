import numpy as np
import math as m
##var4
e = 0.001
y = 0
x = (m.sin(y - 1/2)+1)/2
x3 = 0.4
x4 = 0.6
x5 = 0
x2 = (x3 + x4)/2
y = 3/2 - m.cos(x)
y3 = 0.5
y4 = 0.7
y5 = 0
y2 = (y3 + y4)/2

def function(x2, y2):
    x5 = 0
    y5 = 0
    while abs(x2 - x5)>e or abs(y2 - y5)>e:
        x5 = x2
        x2 = (m.sin(y2 - 1/2)+1)/2
        y5 = y2
        y2 = (3/2 - m.cos(x2))
        print(x2,' ', y2)
    print('Answers are: x = ', x2, ' y = ', y2)
function(x2, y2)
