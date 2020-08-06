# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math as m
from sympy.abc import a, c, x, y, z
Docx, Docy, Docz, Dcax, Dcay, Dcaz = sp.symbols('Docx, Docy, Docz, Dcax, Dcay, Dcaz')


#%%
A = sp.Matrix([[1, 0, 0, Docx + Dcax],
               [0, 1, 0, Docy + Dcay],
               [0, 0, 1, Docz + Dcaz],
               [0, 0, 0, 1]])

B = sp.Matrix([[1,0, 0, 0],
               [0, sp.cos(-a), -sp.sin(-a), 0],
               [0, sp.sin(-a), sp.cos(-a), 0],
               [0, 0, 0, 1]]) #A軸旋轉矩陣

C = sp.Matrix([[1, 0, 0, -Dcax],
               [0, 1, 0, -Dcay],
               [0, 0, 1, -Dcaz],
               [0, 0, 0, 1]])

D = sp.Matrix([[sp.cos(-c), -sp.sin(-c), 0, 0],
               [sp.sin(-c), sp.cos(-c), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]) #C軸旋轉矩陣

E = sp.Matrix([[1, 0, 0, -Docx],
               [0, 1, 0, -Docy],
               [0, 0, 1, -Docz],
               [0, 0, 0, 1]])

V = sp.Matrix([x, y, z, 1])

A_inv= A.inv()


#%%
A_inv


#%%
U_inv = E.inv()*D.inv()*C.inv()*B.inv()*A.inv()*V


#%%
U_inv


#%%
U_inv_sfy = sp.simplify(U_inv)


#%%
U_inv_sfy


#%%
cl2nc = U_inv_sfy.subs({x:-3.045, y:5.4, z:43.041, Docx:0, Docy:0, Docz:0, Dcax:0, Dcay:0, Dcaz:0, a:-29.060*3.1415926/180, c:47.685*3.1415926/180})


#%%
cl2nc


#%%
U_invs = sp.simplify(E.inv()*D.inv()*C.inv()*B.inv()*A.inv()*V)


#%%
U_invs


#%%
cl2nc1 = U_invs.subs({x:-3.045, y:5.4, z:43.041, Docx:0, Docy:0, Docz:0, Dcax:0, Dcay:0, Dcaz:0, a:-29.060*3.1415926/180, c:47.685*3.1415926/180})
cl2nc2 = U_invs.subs({x:2.743, y:5.123, z:32.128, Docx:0, Docy:0, Docz:0, Dcax:0, Dcay:0, Dcaz:0, a:-43.008*3.1415926/180, c:-119.436*3.1415926/180})


#%%
cl2nc1, cl2nc2


#%%



