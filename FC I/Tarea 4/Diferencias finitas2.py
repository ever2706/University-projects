# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:38:40 2021

@author: Ever Ortega Calderón
"""

import numpy as np
import matplotlib.pyplot as plt

def Aproximacion(rho, pm, niter, separacion,D):
    print(rho)
    for iter in range(niter):
        for m in range(1, pm-1, 1): 
            for n in range(1, pm-1, 1):              
                rho[m, n] =(-separacion*rho[m,n+1]+D*(rho[m+1,n]+rho[m-1,n]))/(-separacion+(2))
                #rho[m,n+1]=D*separacion*((rho[m+1,n]-2*rho[m,n]+rho[m-1,n])/(separacion**2))+rho[m,n]
                #rho[m,n+1]=((D*(rho[m+1,n]+rho[m-1,n]))-rho[m,n]*(-separacion+2*D))/separacion
    valorAprox = rho
    return valorAprox

def Grafico(extension, niter):
    D=0.5
    A=2.0
    x0=5
    l=1.5
    
    tiempo=extension
    valor_inicial_x=0
    valor_final_x=0
    
    puntosmalla = 30
    x = np.linspace(0, extension, puntosmalla)
    t = np.linspace(0, tiempo, puntosmalla)
    rhoi = np.zeros((puntosmalla, puntosmalla), float)
    rhoi[0] = A*np.exp(-((x-x0)**2)/l)
    #rhoi[0,0] = valor_inicial_x
    #rhoi[0,puntosmalla-1] = valor_final_x
    
    #for i in range(0, puntosmalla): 
        #rhoi[0,i] = A*np.exp(-((x[i]-x0)**2)/l)
        #rhoi[0,0] = valor_inicial_x
        #rhoi[0,puntosmalla-1] = valor_final_x
        
    
    separacion=10/puntosmalla
  
    Z = Aproximacion(rhoi, puntosmalla, niter,separacion,D)
    print(Z)
    X, T = np.meshgrid(x, t)
    plt.figure(figsize=(10,6))
    ax = plt.axes(projection='3d')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.set_zlabel('Difusión')
    ax.plot_surface(T,X, Z, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
    ax.set_title('Aproximacion potencial electrico en la placa')
    plt.show()
 

 
    return

extension=10
niteraciones=1000
Grafico(extension,niteraciones)
