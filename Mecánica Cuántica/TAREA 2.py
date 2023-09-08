# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:41:18 2021

@author: Ever Ortega Calderón
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h
from scipy.integrate import quad
from mpl_toolkits.mplot3d.axes3d import Axes3D

def Calculo_integral(x,t,a,m):
    h_cortado= h/(2*np.pi)
    imagi=1j
    f= lambda k: np.exp(-k**2/(4*a)) * np.exp(imagi*(k*x-(h_cortado*k**2 *t)/(2*m)))
    resultado_int=quad(f,np.NINF, np.Inf)[0]
    return resultado_int

def Psi(x,t,a,m):
    resultado= (1/(np.sqrt(2*np.pi))) * (1/((2*np.pi*a)**(1/4))) * Calculo_integral(x,t,a,m)
    return resultado

def Grafico_interactivo(x,t,a,m):
    puntosmalla = 30
    posicion = np.linspace(0, x, puntosmalla)
    tiempo = np.linspace(0, t, puntosmalla)
    X, Y = np.meshgrid(posicion, tiempo)
    
    Z=Psi(x,t,a,m)
    
    plt.figure(figsize=(10,6))
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('U (V)')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='cividis', edgecolor='none')
    ax.set_title('Aproximacion potencial electrico en la placa')
    plt.show()
 
    return

def Grafico (x,t,a,m):
    espaciado=100
    fig = plt.figure()
     
    axes3d = Axes3D(fig)
     
     #! Fideos
    posicion = np.linspace(0,x,espaciado)
    tiempo = np.linspace(0,t,espaciado)
     
    X,Y = np.meshgrid(posicion,tiempo)
    Z= Psi(X,Y,a,m)
     
    axes3d.plot_surface(X,Y,Z)


print (Calculo_integral(1,1,1,1))
print( Psi(1,1,1,1))
Grafico(1,1,1,1)