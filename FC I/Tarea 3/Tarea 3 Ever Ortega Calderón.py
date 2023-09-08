# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:53:32 2021

@author: Ever Ortega Calderón
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import wavfile
from scipy.fft import fft
from scipy.fft import fftfreq

"""
Se genera la señal ruidosa, importando un audio
"""
#ruta= "C:/Users/Ever Ortega Calderón/Documents/TEC/I S 2021/FC I/Tarea 3/twins.wav"
ruta= "C:/Users/Ever Ortega Calderón/Documents/TEC/I S 2021/FC I/Tarea 3/jesus1.wav"

tasa_muestreo, valores_x = wavfile.read(ruta)

fig, ax = plt.subplots(1, 1, dpi=120)
ax.plot(valores_x)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.set_title('Señal de audio')
plt.show()

"""
Se calcula la transformada de Fourier de la señal de entrada
"""
# Aplicación de la transformada
deltaT=1
nPuntos=deltaT*tasa_muestreo
puntos_frecuencia = np.linspace (0.0, 512, int(nPuntos/2))

# Se aplica la transformada rapida a la señal
transformada_señal = fft(valores_x)
print(transformada_señal)

amplitudes = (2/nPuntos)*np.abs(transformada_señal[0:np.int(nPuntos/2)])

fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_frecuencia, amplitudes)
ax.set_title('Señal en el dominio de la frecuencia')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud')
ax.set_xticks(np.arange(0,501,50))
plt.show()


from scipy.fft import ifft

#Se aplica la transformada rápida a la señal transformada
puntos_tiempo=np.linspace(0,deltaT,nPuntos)
transformada_inversa_señal=ifft(transformada_señal)

fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_tiempo[1:50], transformada_inversa_señal[1:50])
ax.set_title('Señal filtrada')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
#ax.set_xticks(np.arange(0,501,50))
plt.show()


"""
fig, ax = plt.subplots(1, 1, dpi=120)
pxx,  freq, t, cax = ax.specgram(valores_x)
fig.colorbar(cax).set_label('Intensidad')
ax.set_xlabel('tiempo')
ax.set_ylabel('Frecuencia')
ax.set_title('Espectrograma')
plt.show()



n = len(valores_x)
T = 1/tasa_muestreo

yf = fft(valores_x)
xf = fftfreq(n, T)
# yf = fft(valores_x)
# xf = np.linspace(0.0, 1.0/(2.0*T), int(n/2))
fig, ax = plt.subplots(1,1,dpi=120)
ax.plot(xf, np.abs(yf))
plt.show()

"""