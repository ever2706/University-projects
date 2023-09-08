# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 00:00:05 2021

@author: Ever Ortega Calderón
"""
"""
Se importan las librerías respectivas:
    Scipy:para emplear RK45
    Numpy:para funciones específicas como el uso de linspace
"""
import scipy.integrate as spint
import numpy as np
import matplotlib.pyplot as plt 

valor_inicial_altura=0.0
valor_inicial_presion=101325.0

#MÉTODO RK4


"""
Esta función se encarga de crear los puntos que serán la altura
Se le solicita al usuario los valores donde quiere que empiece y termine el análisis de la altura
Se contempla la posibilidad de solo querer un punto
Se hace control de errores al interactuar con el usuario
La función retorna:
        y=los puntos de altura espaciados según el rango que el usuario considerara
        separacion_altura=la separación que el usuario deseea en sus puntos
        altura_ini=corresponde al valor inicial de altura que desea el usuario
        altura_fin=valor final de altura que el usuario desea en su análisis
        
"""
def Altura():

    while True:
        try:
            altura_ini=float(input("Digite la altura inicial: "))
            altura_fin=float(input("Digite la altura final, en dado caso de querer solo un punto ingrese el mismo valor de altura inicial: "))
            if altura_ini==altura_fin:
                print("Usted seleccionó el mismo valor de altura inicial y final, por ende la separación automática será cero, pues desea solo un punto")
                break
            else:
                if altura_ini<0 or altura_fin<0:
                    print("La altura se mide sobre el nivel del mar, no puede ser negativa, intentelo de nuevo")
                    pass
                else:
                    break
        except:
            print("Introdujo un dato que no es aceptable, reintentelo")
            pass
#Aquí se solicita la separación deseada para crear un arreglo que obtenga los puntos de altura a analizar
    while True:
        if altura_ini==altura_fin:
            separacion_altura=1
            cant_puntos=1
            y=np.linspace(altura_ini,altura_fin,1)
            break
        try:
            separacion_altura=float(input("Digite la separación en la altura que desea: "))
            if separacion_altura==0 :
                print("La altura no puede poseer una separación de cero, intentelo de nuevo")
                pass
            else:
                cant_puntos=int((altura_fin-altura_ini)/separacion_altura)
                y=np.linspace(altura_ini,altura_fin,cant_puntos+1)
                break 
        except:
            print("Introdujo un dato de separación que no es aceptable, reintentelo")
            pass  
    return y,separacion_altura,altura_ini,altura_fin,cant_puntos
    
"""
Función que crea el valor de temperatura en una altura en particular
Entra:
    y=altura deseada en el punto de análisis
Retorna:
    temperature=el valor de temperatura 
"""
def Temperatura(y):
    temperature=293.0 - y/200.0
    return temperature    

"""
Función que crea la densidad de atmósfera
Entra:
    P=hace referencia al y(t) en la EDO y corresponde a los valores de presión
    y= corresponde al t en la EDO y corresponde a las alturas
Retorna:
    f=el valor de densidad de atmósfera
"""
def F_densidad(P,y):
    f=(0.0289647/(8.314462*Temperatura(y)))*P
    return f
"""
Función que crea el lado derecho de la EDO que se desea resolver
Entra:
    P=hace referencia al y(t) en la EDO y corresponde a los valores de presión
    y= corresponde al t en la EDO y corresponde a las alturas
Retorna:
    f=hace refencia al valor de la densidad de atmosfera por g, el lado derecho como tal de la EDO
"""

def Lado_derecho(P,y):
    f=-(F_densidad(P,y))*9.8
    return f

"""
Función que calcula los ks y retorna la estimación de la presión
Entra:
    altura=el valor de altura anterior al del análisis en cuestión
    presión=el valor de presión anterior al del análisis en cuestión
    h=la separación entre los puntos del intervalo en análisis
    lado_derecho= hace referencia al lado derecho de la EDO, el f(y(t),t)
Retorna:
    pres=el valor de presión nuevo, la nueva estimación
"""
def Calculo_ks(altura,presion,h,Lado_derecho):
    k1=h*Lado_derecho(presion, altura)
    k2=h*Lado_derecho(presion+k1/2,altura+h/2)
    k3=h*Lado_derecho(presion+k2/2,altura+h/2)
    k4=h*Lado_derecho(presion+k3,altura+h)
    pres=presion+((k1+2*k2+2*k3+k4)/6)
    return pres


    
#Se llaman las funciones pertinentes

ys,h,altura_inicial,altura_final,cant_puntos=Altura()
#Arreglo que contendrá la solución numérica de la EDO, según las alturas en análisis, se inicializa su primer valor en el valor inicial de presion sobre el nivel del mar
presiones=[valor_inicial_presion]

for i in range(0,len(ys)-1):
   nueva_presi=Calculo_ks(ys[i],presiones[i],h,Lado_derecho) 
   presiones.append(nueva_presi)
   
#Se muestra al usuario los valores de la solución numérica por el método de RK4
print()
print("La solución numérica buscada por medio de RK4 es: ")
print(presiones)

#MÉTODO RK45
"""
Funcion F define la función lado derecho de la EDO
Entra:
    y=valores de altura correspondientes al t en la f
    P=valores de presión correspondientes al y(t) en la f
    Se tiene el cuidado de meter los parámetros a la función en el orden correcto que pide RK45
Retorna:
    La función del lado derecho de la EDO    
"""
def F(y,P):
    M=0.0289647
    R=8.314462
    g=9.8
    valorf=-((M*P*g)/(R*(293-y/200)))
    return valorf

#Se ordena lo pertinente para el método, se usan los valores de altura que ingresó el usuario para inicializar el intervalo de valores que requiere el método
ys_rk45=np.linspace(altura_inicial,altura_final,cant_puntos+1)
metodoRK = 'RK45'
presiones_RKscipy= spint.solve_ivp(F, [altura_inicial,altura_final] , [valor_inicial_presion],t_eval=ys_rk45,method=metodoRK)
ys_de_rk45=presiones_RKscipy.t

#Se muestra al usuario los valores de la solución numérica por el método de RK45 de Scipy
print()
print("Las presiones por medio de RK45 son: ")
print(presiones_RKscipy.y[0])

#Solución analítica
"""
Función Sol_analitica que contiene la solución analítica de la EDO
Entradas:
    El valor de altura
Retorna:
    El valor de presión correspondiente a la altura que entró
"""
def Sol_analitica(altura):
    presiones_analiticas=np.exp(-200*-0.03413979882*np.log(np.absolute(altura-58600))-63.43459957)
    return presiones_analiticas

#Se crea presiones_analicas_valores que es un arreglo que contiene los resultados de evaluar cada valor de altura deseado en la solución analítica y la función Sol_analitica
presiones_analiticas_valores=[valor_inicial_presion]
for i in range(1,len(ys_rk45)):
    presiones_analiticas_valores.append(Sol_analitica(ys_rk45[i]))
#Se muestran los resultados analíticos para posteriormente compararlos con los métodos numéricos
print()
print("Las presiones producto de la solución analítica son: ")
print(presiones_analiticas_valores)


#Gráfico
fig, ax = plt.subplots(dpi=120)
ax.plot(ys, presiones, label='Aprox RK4')
ax.plot(ys_de_rk45, presiones_RKscipy.y[0], label='Aprox RK45')
ax.plot(ys,[Sol_analitica(i) for i in ys], label="Solución analítica")
ax.set_xlabel("Altura")
ax.set_ylabel("Presión")
plt.legend(loc='best', prop={'size':10})
plt.title('Solución numérica de la EDO')
plt.show()