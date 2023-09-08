# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 13:28:47 2021

@author: Ever Ortega Calderón
"""

#Se importan las librerías necesarias
#Matplotlib para gráficos
#Numpy para algunas situaciones matemáticas 
#De scipy.constants se importa la constante de Planck
#De scipy.integrate se importa quad para poder resolver las ecuaciones 
from sympy import Derivative, Symbol
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h
from math import e
import math
from sympy import *

#Se definen las constantes del problema
h_cortado= h/(2*np.pi)
m=1.67*10**(-27)
w=1

#Se define la x cómo variable simbólica
x=Symbol("x")

"""
Función Estado_base: define el estado Psi0, el cuál es el estado de base para el oscilador armónico cuántico
    Entradas: 
        Ninguna
    Salidas: 
        psi_0= El estado base del problema 
         
"""
def Estado_base():
    psi_0=(m*w/np.pi*h_cortado)**(1/4) * e**((-m*w*(x**2))/2*h_cortado)
    return psi_0

"""
Función Aplicar_operador_1vez : aplica el operador de subida a un estado
    Entradas: 
        estado= estado al cuál se le aplicará el operador de subida
    Salidas: 
        operador_aplicado= resultado de aplicar el operador de subida
         
"""
def Aplicar_operador_1vez (estado):
    operador_aplicado= (1/(np.sqrt(2*h_cortado*m*w)))*((-h_cortado*Derivative(estado,x,1).doit()) + m*w*x*estado)
    return operador_aplicado

"""
Función Aplicar_operador_varias_veces: aplica el operador las veces que sean necesarias, según el estado deseado, empleando la función Aplicar_operador_1vez
    Entradas:
        n=estado deseado
    Salidas: 
        resultado_de_aplicar_operador= operador de subida aplicado n veces al estado base
         
"""
def Aplicar_operador_varias_veces(n):
    #Se define el primer estado cómo el estado base
    estado_actual=Estado_base()
    for i in range(0,n):
        #Se aplica el operador al estado n
        resultado_de_aplicar_operador=Aplicar_operador_1vez(estado_actual)
        #Se actualiza el estado según el n que se encuentre
        estado_actual=resultado_de_aplicar_operador
    return resultado_de_aplicar_operador
"""
Función Funcion_final: encargada de formar la función final
    Entradas: 
        n= estado deseado
    Salidas: 
        resultado= función final del estado deseado
         
"""
def Funcion_final(n):
    resultado=(1/np.sqrt(math.factorial(n)))*Aplicar_operador_varias_veces(n)
    return resultado

"""
Función Grafico: encargada de ejecutar la función Psi para todos los valores de posición deseados, en ella se ajusta el valor de t deseado
además ejecuta el gráfico deseado
    Entradas:
        Ninguna
    Salidas:
        Muestra el gráfico de posición contra la función de onda.
         
"""
def Grafico(n):
    #Se definen la cantidad de puntos en los que se divide el espacio
    cant_pts = 30
    X = np.linspace(0, 5, cant_pts)
    funcion_onda=[]
    #Se evalúa la función del estado para cada valor de la posición
    for i in X:
        funcion_onda.append(Funcion_final(n).subs(x,i))
    fig,ax=plt.subplots(dpi=120)
    ax.plot(X, funcion_onda,"b")
    ax.set_title("Función de onda para el oscilador armónico cuántico en el estado " + str(n))
    ax.set_xlabel("Posición")
    ax.set_ylabel("Función de onda")
    plt.show()
"""
Función Energia: calcula la energía del estado deseado
    Entradas: 
        n= estado deseado
    Salidas: 
        valor de energía= valor de energía para el estado deseado
         
"""
def Energia(n):
    valor_energia=(n +0.5)*(h_cortado*w)
    return valor_energia
    
#Se define el estado deseado
n=10
#Se imprime el valor de energía para este estado 
print ("Valor de energía para el estado n=", n, ": ", Energia(n))      
#Se corre la función Grafico
Grafico(n)