# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:08:18 2021

@author: Ever Ortega Calderón
"""
import numpy as np
import scipy.integrate as spint
altura=np.linspace(0,3000,1500)

def F(y,P):
    f=-((28.9647*P)/(8.314462*(293-y/200)))*9.8
    return f


def RK4(f,y0,x0):
    h=2
    M=28.9647
    R=8.314462
    g=9.8
    k1=h*f(y0, x0,M,R,g)
    k2=h*f(y0+k1/2,x0+h/2,M,R,g)
    k3=h*f(y0+k2/2,x0+h/2,M,R,g)
    k4=h*f(y0+k3,x0+h,M,R,g)
    y=y0+(k1+2*k2+2*k3+k4)/6
    return y

metodoRK = 'RK45'
y_aprox_RKscipy = spint.solve_ivp(F, [0,3000], [101325], method=metodoRK)

print(y_aprox_RKscipy.y[0])