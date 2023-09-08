# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:30:04 2021

@author: Ever Ortega Calderón
"""
#Se importan las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy import signal
from scipy.fft import ifft

# Parámetros
tasa_muestreo = 1024
deltaT = 1

# Tamaño del arreglo de muestras
nPuntos = deltaT*tasa_muestreo

# arreglo de puntos para los valores en el tiempo
puntos_tiempo = np.linspace(0, deltaT, nPuntos)
#Frecuencias y magnitudes para cada una de las señales puras
frec_1 = 70
magnitud_1 = 35
frec_2 = 40
magnitud_2 = 60
#Creación de las dos señales 
señal_1 = magnitud_1*signal.square(2*np.pi*frec_1*puntos_tiempo )
señal_2= magnitud_2*signal.sawtooth(2*np.pi*frec_2*puntos_tiempo)
#Suma de las señales individuales para crear la señal pura
señal_pura=señal_1+señal_2
# Ruido para la señal
ruido = np.random.normal(0, 20, nPuntos)
#Suma del ruido más las señales puras, para crear la señal distorsionada a trabajar
señal_ruidosa = señal_1 + señal_2 + ruido
#Gráfico de la señal pura y la ruidosa
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=120, sharey= True)
ax1.plot(puntos_tiempo[0:50], señal_pura[0:50])
ax1.set_title('Señal original')
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Amplitud')

ax2.plot(puntos_tiempo[1:50], señal_ruidosa[1:50])
ax2.set_title('Señal ruidosa')
ax2.set_xlabel('Tiempo')
plt.show()
##############################################################################  Fin primer punto
# Aplicación de la transformada
puntos_frecuencia = np.linspace (0.0, 512, int(nPuntos/2))
# Se aplica la transformada rapida a la señal
transformada_señal = fft(señal_ruidosa)
#Amplitudes de los valores de frecuencia
amplitudes = (2/nPuntos)*np.abs(transformada_señal[0:np.int(nPuntos/2)])
#Gráfico de la transforma el dominio de la frecuencia
fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_frecuencia, amplitudes)
ax.set_title('Señal en el dominio de la frecuencia')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud')
ax.set_xticks(np.arange(0,501,50))
plt.show()
######################################################### Fin segundo punto
"""
Función Filtrar_Señal filtra las señales que se consideren como ruido
    Recibe:
        señal:las amplitudes de cada frecuencia de la transformada
        transformda: la transformada de fourier de la señal ruidosa
        umbral: indica una amplitud de referencia para el filtrado de la señal 
    Retorna:
        transformada: los valores de la transforma de Fourier de la señal ruidosa, pero con los valores considerados como ruido eliminados y definidos como cero
        Gráfico: la función grafica la transforma en el dominio de la frecuencia, pero sin el ruido
        
"""
def Filtrar_Señal(señal,transformada,umbral):
    for i in range(len(señal)):
        if señal[i]<umbral:
            transformada[i]=0.0 +0.0j
            señal[i]=0.0
    puntos_frecuencia=np.linspace(0.0,512,int(nPuntos/2))
    fig,ax=plt.subplots(dpi=120)
    ax.plot(puntos_frecuencia,señal)
    ax.set_title("Señal en el dominio de la frecuencia")
    ax.set_xlabel("Frecuencia [Hz]")
    ax.set_ylabel("Amplitud")
    ax.set_xticks(np.arange(0,501,50))
    plt.show()
    return transformada
#Se define el umbral sobre el cual cualquier amplitud inferior se considerará ruido
umbral=21
#Se llama a la función Filtrar_Señal y se asigna su retorno a una nueva variable que representa la señal filtrada en el dominio de la frecuencia
señal_filtrada=Filtrar_Señal(amplitudes,transformada_señal,umbral)

##################################################### Fin tercer punto
#Se aplica la transformada rápida a la señal transformada
transformada_inversa_señal=ifft(señal_filtrada)

#Se grafica la señal filtrada en el dominio temporal
fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_tiempo[1:50], transformada_inversa_señal[1:50])
ax.set_title('Señal filtrada en el dominio del tiempo')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
plt.show()

######################################## Fin cuarto punto