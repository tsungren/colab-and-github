# https://www.youtube.com/watch?v=3jTRuqtTPts
# 基礎sympy教學
# 張譽瀚

from sympy import init_printing
init_printing(use_unicode=False,
              wrap_line=False, no_global=True)

import sympy as sp
x = sp.Symbol('x')
#x = sp.Symbol('x', real = True) 其中real = True是令x為實數real
y = sp.Symbol('y')

print(sp.diff(x+2*y,y))

print(sp.integrate(sp.cos(x), (x,-1,1)))

print(sp.solve((2*x+5*y+1, 13*x+25*y+64),x,y))
'''
A = sp.solve(x**5+2*x**4-2*x**3+7*x**2+9*x+123,x)
for i in A:
    print(sp.N(i))
'''
print(sp.limit(1/x, x, 'oo'))

print(sp.cos(x**2).series(x, 0, 10)) #Taylor泰勒展開式

print(sp.together(1/x + 1/y))

print(sp.summation(1/x,(x, 1, 2)))

print(sp.solve(y**4-1,y))

# https://www.youtube.com/watch?v=kx2GzBeGPco
# SymPy (Symbolic Expressions on Python) in one video
# Ahmad Bazzi：# 40:56 Solving a system of non-linear equations
# 未完待續，影片太長前面沒看後面做不出來
A = sp.Matrix(((1,1,1), (1,1,2), (2,1,-1)))
b = sp.Matrix(((1),(3),(10)))
system = A, b
ls = sp.solve(system)
print(ls)

# https://www.youtube.com/watch?v=3PGQS6hzThc&list=PLpltJwWB6egJD0bCPdYsGwn9TeY_10vB3&index=53
# Yen-Lung Tsai
# 53/229

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#符號型的計算




