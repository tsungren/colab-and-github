#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math as m
#設定a, c, x, y, z, Docx, Docy, Docz, Dcax, Dcay, Dcaz為符號,以利符號運算
from sympy.abc import a, c, x, y, z 
Docx, Docy, Docz, Dcax, Dcay, Dcaz = sp.symbols('Docx, Docy, Docz, Dcax, Dcay, Dcaz')

'''
RoC = sp.Matrix([[sp.cos(c), -sp.sin(c), 0],
                 [sp.sin(c), sp.cos(c), 0],
                 [0, 0, 1]])
RoA = sp.Matrix([[1,0, 0],
                 [0, sp.cos(a), -sp.sin(a)],
                 [0, sp.sin(a), sp.cos(a)]])
'''

toolvec = ([2, 5, 9])
i = toolvec[0]/(m.sqrt(toolvec[0]**2+toolvec[1]**2+toolvec[2]**2))
j = toolvec[1]/(m.sqrt(toolvec[0]**2+toolvec[1]**2+toolvec[2]**2))
k = toolvec[2]/(m.sqrt(toolvec[0]**2+toolvec[1]**2+toolvec[2]**2))

radA1 = m.acos(k) #A角第1解的弳度值
radA2 = -m.acos(k) #A角第2解的弳度值

radC1 = m.atan2(i/m.sin(radA1), -j/m.sin(radA1)) #C角第1解的弳度值
radC2 = m.atan2(i/m.sin(radA2), -j/m.sin(radA2)) #C角第2解的弳度值

A = sp.Matrix([[1, 0, 0, Docx + Dcax],
               [0, 1, 0, Docy + Dcay],
               [0, 0, 1, Docz + Dcaz],
               [0, 0, 0, 1]])

B = sp.Matrix([[1,0, 0, 0],
               [0, sp.cos(-a), -sp.sin(-a), 0],
               [0, sp.sin(-a), sp.cos(-a), 0],
               [0, 0, 0, 1]])

C = sp.Matrix([[1, 0, 0, -Dcax],
               [0, 1, 0, -Dcay],
               [0, 0, 1, -Dcaz],
               [0, 0, 0, 1]])

D = sp.Matrix([[sp.cos(-c), -sp.sin(-c), 0, 0],
               [sp.sin(-c), sp.cos(-c), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])
E = sp.Matrix([[1, 0, 0, -Docx],
               [0, 1, 0, -Docy],
               [0, 0, 1, -Docz],
               [0, 0, 0, 1]])

V = sp.Matrix([x, y, z, 1])


U = A*B*C*D*E*V

point01=U.subs({x:50, y:35, z:25, Docx:5, Docy:10, Docz:20, Dcax:-10, Dcay:-5, Dcaz:-15, a:radA1, c:radC1})
point02=U.subs({x:50, y:35, z:25, Docx:5, Docy:10, Docz:20, Dcax:-10, Dcay:-5, Dcaz:-15, a:radA2, c:radC2})

print(point01)
print(point02)

#print(radA1, radC1, radA2, radC2)

print(m.degrees(radA1), m.degrees(radC1), m.degrees(radA2), m.degrees(radC2) )





