# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:35:47 2021

@author: Ever Ortega Calderón
"""
"""
#RK4

def f(y,x):
    valorF=x+y*y
    return valorF

def RK4(f,y0,x0,x):
    h=x-x0
    k1=h*f(y0, x0)
    k2=h*f(y0+k1/2,x0+h/2)
    k3=h*f(y0+k2/2,x0+h/2)
    k4=h*f(y0+k3,x0+h)
    y=y0+(k1+2*k2+2*k3+k4)/6
    return y

x0=0
y0=0
x=0.3    

#no puedo imprimir lo que me devuelve la función RK4 de huevazo, necesito darle el resultado a una variable, 
#porque me devuelve un número y eso no puedo llamarlo y devolverlo tal cual, int is not callable
resultado=RK4(f,y0,x0,x)

print("Compa el resultado que usted busca es: "+str(resultado))


#RK45

import scipy.integrate as spint

def f(x,y):
    valorF=x+y*y
    return valorF
x0=0
y0=0
x=0.3 

#esta vara debe recibir los parámetros de la función en orden primero t y después y(t) 
#Los valores iniciales deben ir en arreglo
resultado=spint.solve_ivp(f,[x0,x],[y0],method="RK45")
#se dice que todo lo que quedó en resultado es una biblioteca, por eso es que para llamar algo específico lo llamo con punto
resultado_de_interes=resultado.y[0][len(resultado.y[0])-1]

#el último en el arreglo de resultados es la solución que busco porque definí el intervalo de 0-0.3 y busco el resultado de 0.3
print("Compa el resultado que usted busca es: "+str(resultado_de_interes))

"""
#RK23

import scipy.integrate as spint

def f(x,y):
    valorF=x+y*y
    return valorF
x0=0
y0=0
x=0.3 

#esta vara debe recibir los parámetros de la función en orden primero t y después y(t) 
#Los valores iniciales deben ir en arreglo
resultado=spint.solve_ivp(f,[x0,x],[y0],method="RK23")
#se dice que todo lo que quedó en resultado es una biblioteca, por eso es que para llamar algo específico lo llamo con punto
resultado_de_interes=resultado.y[0][len(resultado.y[0])-1]

#el último en el arreglo de resultados es la solución que busco porque definí el intervalo de 0-0.3 y busco el resultado de 0.3
print("Compa el resultado que usted busca es: "+str(resultado_de_interes))

