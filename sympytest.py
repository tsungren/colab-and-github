#from sympy.interactive import printing
import numpy as np
import sympy as sp
from random import random

#def f(x):
#    return np.sin(x)

func = sp.Function('func')
func1 = sp.Function('func1')
func2 = sp.Function('func2')
x = sp.Symbol('x')

func = x**3 + 2*x**2 + 3*x + 4
func1  = sp.cos(x) + 2*sp.sin(x) - 2
func2  = x**3 + x*sp.sin(x) + 3
print("display my function")
print(func, func1, func2)

'''
inte = sp.Integral(func,x)
inte1 = sp.Integral(func1,x)
inte2 = sp.Integral(func2,x)
print("display function integral")
print(inte, inte1, inte2)


print("evaluate integral")
answer = sp.integrate(func,x)
#answer1 = sp.integrate(func1,x)
#answer2 = sp.integrate(func2,x)
print(answer, answer1, answer2)
'''

print("evaluate differential")
derivative = sp.diff(func,x)
derivative1 = sp.diff(func1,x)
derivative2 = sp.diff(func2,x)
print(derivative, derivative1, derivative2)
#print(derivative)


i = 0
z = 1
#z = random()
maxiter = 3

while( abs(func1.subs(x, z)) > 1e-8 or i < maxiter ):
    i = i + 1
    z = z - ( func1.subs(x, z)/derivative1.subs(x, z) )
    #print(func.subs(x, z))
    #print(derivative.subs(x, z))

print(sp.N(z))
