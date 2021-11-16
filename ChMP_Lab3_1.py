import math

def func(x):
    f = x**4+4*x**3-8*x**2-17
    return f
def deriv1(x):
    deriv = 4*x**3-12*x**2-16*x
    return deriv
def deriv2(x):
    doubleDeriv = 12*x**2-24*x-16
    return doubleDeriv

def NeutonMethod(a, b, e):
    if func(b)*deriv2(b)>0: ##дізнаємося, з якого боку працювати
        x = b
    else:
        x = a
    h = func(x)/deriv1(x)
    x = x-h
    if abs(h) <= e:
        print (x)
    else:
        h = func(x)/deriv1(x)
        x = x-h
        print ("The answer is ", x)
        

NeutonMethod(-6, -4, 0.0001)
NeutonMethod(1, 3, 0.0001)


