import math

def func(x):
  f = x**4 + 4*x**3 - 8*x**2 - 17
  return f
def hordMethod(a,b,e):
    while abs(b-a)>e:
        if func(a)*func((a+b)/2)<0:
            b = (a+b)/2
        else:
            a = (a+b)/2
    x = (a+b)/2
    print("The answer is ", x)
a = -6
b = -4
e = 0.0001
hordMethod(a, b, e)
