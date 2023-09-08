# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:50:50 2021

@author: Ever Ortega Calderón
"""

import numpy as np
#import scipy.integrate as spint
import matplotlib.pyplot as plt


def Parte_temporal(A,x0,l,n,D,t,x):
    valor_temporal=A*np.exp(-((x-x0)**2/(l))-((((n*np.pi)/(10*np.sqrt(1/D))))**2)*t)
    return valor_temporal


def Parte_espacial(n,D,x):
    valor_espacial=np.sin(((n*np.pi)/(10*np.sqrt(1/D)))*x)
    return valor_espacial

def Grafico(x,t,z):
    X, T = np.meshgrid(x, t)
    plt.figure(figsize=(10,6))
    ax = plt.axes(projection='3d')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.set_zlabel('Difusión')
    ax.plot_surface(T,X, z, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
    ax.set_title('Aproximacion potencial electrico en la placa')
    plt.show()

#Se definen las constantes a usar
A=2
l=1.5
x0=5
D=0.5
lx=10
lt=lx
separacion=100
#Se definen los valores de tiempo para trabajar
t=np.linspace(0,lt,separacion)
#Se definen los valores de x para trabajar
x=np.linspace(0,lx,separacion)
rho=np.zeros((len(x),len(t)))

for i in range(0,len(t)):
    for j in range(0,len(x)):
        rho[i,j]=Parte_temporal(A,x0,l,1,D,t[i],x[j])*Parte_espacial(1,D,x[j])
        
#print (rho)
Grafico(x,t,rho)
    

