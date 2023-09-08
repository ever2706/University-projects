# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:04:33 2021

@author: Ever Ortega Calderón
"""

#Se importan las librerías necesarias
#Matplotlib para gráficos
#Numpy para algunas situaciones matemáticas 
#De scipy.constants se importa la constante de Planck
#De scipy.integrate se importa quad para poder resolver las ecuaciones 
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h
from scipy.integrate import quad


"""
Función Calculo_integral: encargada de calcular la integral que se encuentra en la función de onda que se desea representar
    Entradas: 
        x: valor de posición
        t=valor de tiempo
        a= constante real y positiva
        m=masa de la partícula
    Salidas: 
        resultado_int=resultado de la integral 
"""
def Calculo_integral(x,t,a,m):
    h_cortado= h/(2*np.pi)
    imagi=1j
    f= lambda k: np.exp(-k**2/(4*a)) * np.exp(imagi*(k*x-(h_cortado*k**2 *t)/(2*m)))
    resultado_int,error=quad(f,np.NINF, np.Inf)
    return resultado_int

"""
Función Psi : Encargada de calcular el valor de la función de onda
    Entradas:
        x: valor de posición
        t=valor de tiempo
        a= constante real y positiva
        m=masa de la partícula
    Salidas:
        resultado=valor de la función de onda
"""
def Psi(x,t,a,m):
    resultado= (1/(np.sqrt(2*np.pi))) * (1/((2*np.pi*a)**(1/4))) * Calculo_integral(x,t,a,m)
    return resultado

"""
Función Grafico: encargada de ejecutar la función Psi para todos los valores de posición deseados, en ella se ajusta el valor de t deseado
además ejecuta el gráfico deseado
    Entradas:
        Ninguna
    Salidas:
        Muestra el gráfico de posición contra la función de onda.
"""
def Grafico():
    puntosmalla = 30
    X = np.linspace(0, 5, puntosmalla)
    tiempo =10
    a=2
    m=1.67*10**(-27)
    funcion_onda=[]
    for i in X:
        funcion_onda.append(Psi(i,tiempo,a,m))
    fig,ax=plt.subplots(dpi=120)
    ax.plot(X, funcion_onda,"b")
    ax.set_title("Función de onda para una partícula libre")
    ax.set_xlabel("Posición")
    ax.set_ylabel("Función de onda")
    plt.show()

#Se ejecuta la función Grafico
Grafico()