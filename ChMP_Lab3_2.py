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

def combMethod(a, b, e):
    if deriv1(a)*deriv2(a)>0: ##>: зліва хорди, зправа дотичні; <: навпаки
      a0 = b
      b0 = a
    else:
      a0 = a
      b0 = b
    xp1 = a0 ## xp1 - an, xp2 - bn
    xp2 = b0
    xn1 = xp1 - (func(xp1)*(xp2-xp1)/(func(xp2)-func(xp1)))
    xn2 = xp2 - func(xp2)/deriv1(xp2)
    xp1 = xn1
    xp2 = xn2
    while (xp2-xp1)<e:
        xn1 = xp1 - (func(xp1)*(xp2-xp1)/(func(xp2)-func(xp1)))
        xn2 = xp2 - func(xp2)/deriv1(xp2)
        xp1 = xn1
        xp2 = xn2
    x = (xp1+xp2)/2
    print("The answer is ", x)

combMethod(-6, -4, 0.0001)