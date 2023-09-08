# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:39:31 2021

@author: Ever Ortega Calderón
"""


#Se define la función a trabajar
def crear_funcion(valor):
    return (0.01/2)*valor*valor-5
#se solicita la aproximación inicial que el usuario desea para la raíz de la función así como el h para el calculo de la derivada
#Variable control se usa para iterar en caso de error introduciendo algún dato y que el usuario tenga la posibilidad de volver a ingresarlo

control=0
while control==0:
    try:
        aproximacion=float(input("Ingrese la aproximación inicial que desea: "))
        h=float(input("Ingrese el valor h que desea para el cálculo de la derivada: "))
        control=1
    except:
        print("Ingrese un número valido, por favor ingrese de nuevo")
#se solicita al usuario la cantidad de iteraciones que desea en el proceso
control=0
while control==0:
    try:
        iteraciones=int(input("Ingrese la cantidad de iteraciones que desea para su raíz: "))
        control=1
    except:
        print("Ingrese un número valido, por favor ingrese de nuevo")

#Se ejecuta el procedimiento de Newton-Raphson
#aproximacion-funcion es la imagen de la raiz actual bajo la funcion 
#aproximacion_derivada es la imagen de la raiz actual bajo la funcion
#en el tercer paso se actualiza el valor de la raíz haciendole la corrección del método
for i in range(0,iteraciones):
    aproximacion_funcion=crear_funcion(aproximacion)
    aproximacion_derivada=(crear_funcion(aproximacion+h)-crear_funcion(aproximacion-h))/(2*h)
    aproximacion=aproximacion-(aproximacion_funcion/aproximacion_derivada)
#Se muestra el resultado al usuario
print("Su aproximación a la raíz de la función es: " + str(aproximacion))
