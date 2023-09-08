# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:06:04 2021

@author: Ever Ortega Calderón
"""
#Se importa la librería numpy que ayudará a crear el arreglo de las x
import numpy as np
#Se importa la biblioteca sympy para trabajar con la x como variable simbólica
import sympy as sp


x=sp.Symbol("x")

#Se le solicitan los parámetros del caso al usuario
#Variable control se usa para iterar en caso de error introduciendo algún dato y que el usuario tenga la posibilidad de volver a ingresarlo
control=0
while control==0:
    try:
        velocidad_inicial=float(input("Ingrese la velocidad inicial: "))
        velocidad_final=float(input("Ingrese la velocidad final: "))
        tiempo_inicial=float(input("Ingrese el tiempo inicial por favor: "))
        tiempo_final=float(input("Ingrese el tiempo final por favor: "))
        control=1
    except:
        print("Los parámetros deben ser números, ingrese de nuevo por favor")
#Con los datos del usuario se crea la funcion lineal de velocidad para el cálculo de la integral númerica
def creacion_funcion(x,velocidad_inicial,velocidad_final,tiempo_inicial,tiempo_final):
    pendiente=(velocidad_inicial-velocidad_final)/(tiempo_inicial-tiempo_final)
    interseccion=velocidad_inicial-pendiente*tiempo_inicial
    return pendiente*x+interseccion

#Se establecen los que serán los límites de la integral
a=tiempo_inicial
b=tiempo_final 

#Si los límites se introducieron al réves entonces se cambian
if a>b:
    print("El orden de los límites ingresados se ha invertido para asegurar un resultado correcto, siendo el menor el inferior y el mayor el superior")
    variable_momentanea=a
    a=b
    b=variable_momentanea
control=0

#Se pide la cantidad de puntos, se revisa que se ingrese un número válido
#N=cantidad de puntos
while control==0:
    try:  
        N=int(input("Ingrese la cantidad de puntos deseados, recuerde que estos son la cantidad se subintervalos deseados menos uno: "))
        if N==1:
            print("N no puede ser 1, esto causará una indefinición en división por cero en el cálculo de h, ingrese de nuevo por favor")
            control=0
        else:
            control=1
    except:
        print("Ingrese un número, por favor")
#Si N es un número par se solicita que sea impar, pues se requiere para el método
while N>=0:
    if N % 2==0:
        print("El número de puntos debe ser impar pues se ejecutará Simpson y no puede ser cero, vuelvalo a ingresar por favor")
        N=int(input("Ingrese la cantidad de puntos deseados, recuerde que estos son la cantidad se subintervalos deseados menos uno: "))
   
    else:
        break
    
#en este momento a y b ya son números por ende el cálculo de h se hace forma directa
#h=espaciado que habrá entre puntos
h=(b-a)/(N-1)

#se crea un arreglo con las preimágenes, es decir los puntos en eje de las abscisas, con ayuda de un numpy:

preimagenes=np.linspace(a,b,N)

#Se crea un arreglo que se llama imagenes, con la intencion de almacenar los correspondientes valores de las ordenadas que corresponden al arreglo preimagenes

imagenes=[]
for i in preimagenes:
    imagenes.append(creacion_funcion(i,velocidad_inicial,velocidad_final,tiempo_inicial,tiempo_final))

#Se usa la ecuación de Simpson para saber el resultado de la integral
#resultado es la variable que guardará el resultado de la integral, siguiendo la formula de la regla de Simpson 
resultado=imagenes[0]+imagenes[N-1]
for i in imagenes:
    if imagenes.index(i) % 2 !=0 and imagenes.index(i)!=0 and imagenes.index(i)!=(N-1) :
        resultado= resultado+(4*i)
        
    if imagenes.index(i) % 2 ==0 and imagenes.index(i)!=(N-1) and imagenes.index(i)!=0 :
        resultado=resultado+(2*i)
        
    
resultado=resultado*(h/3)

#se le muestra al usuario el resultado
print("El resultado de la integral es: "+str(resultado))