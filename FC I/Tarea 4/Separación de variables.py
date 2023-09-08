# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:56:30 2021

@author: Ever Ortega Calderón
"""


import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

def F0F1 (x,y):
    D=0.5
    valorF0F1=[y[1], -1/(D) *y[0]]
    return valorF0F1

def Parte_espacial():
    y=np.zeros(0)
    xi=0
    xf=10
    n=100
    x=np.linspace(xi,xf,n)
    
    y0=0
    y1=0
    
    metodoRK= "RK45"
    solucion_sistema_EDO=spint.solve_ivp(F0F1,[xi,xf],[y0,y1],t_eval=x,method=metodoRK)
    return solucion_sistema_EDO

print(Parte_espacial())
