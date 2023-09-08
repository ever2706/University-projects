# Fourier series analysis for a square wave function
# user defined function

# Tomado de
# https://vcfw.org/pdf/Department/Physics/Fourier_series_python_code.pdf

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.integrate import simps

#===============================================================
def Analisis_Fourier(puntos_X, puntos_Y, terms):
    """
    puntos_X, puntos_Y: arreglos unidimensionales con las coordenadas de la señal a aproximar
    terms: entero que indica el número de términos a sumar en la serie de Fourier

    Pseudocódigo:
    1. Calcule el coeficiente a_0.
    2. Inicialice un arreglo lleno de ceros llamado suma_Fourier. En este arreglo se almacenarán
       los valores de la serie de Fourier para cada coordenada x.
    3. Inicialice un ciclo que se recorrerá tantas veces como términos se quieren usar
       para la aproximación.
    3.1. Calcule los coeficientes a_n y b_n para el n-ésimo término de la serie usando
         la función Cálculo_Coeficientes()
    3.2. Calcule el valor de la suma de Fourier para cada valor de x
    3.3. Sume el valor obtenido en el paso 3.3 al arreglo suma_Fourier

    4. Sume a_0/2 a cada entrada de suma_Fourier
    5. Retorne el arreglo suma_Fourier
    """
    # Cálculo de los coeficientes de Fourier
    coeficiente_a_0 = (2./periodoL)*simps(puntos_Y, puntos_X)

    suma_Fourier = np.zeros(nMuestras)
    
    for iContador in range(1, terms+1):
        coeficientes_a, coeficientes_b = Calculo_Coeficientes(iContador, puntos_X, puntos_Y)

        suma_Fourier += coeficientes_a*np.cos(2.*np.pi*iContador*puntos_X/periodoL) +\
                        coeficientes_b*np.sin(2.*np.pi*iContador*puntos_X/periodoL)
        
        
    
    return suma_Fourier + coeficiente_a_0/2.


#===============================================================
def Calculo_Coeficientes(contadorN, array_X, array_Y):
    """
    contadorN: entero, n-ésimo término de la serie
    arreglo_x, arreglo_Y: arreglos unidimensionales con las coordenadas de la señal a aproximar

    Pseudocódigo:
    1. Inicialice dos arreglos donde se almacenarán los coeficientes a_n y b_n para cada coodenada x
    2. Calcule los valores de los coeficientes a_n y b_n para cada coordenada x
    3. Retorne los arreglos con los coeficientes a_n y b_n
    """
    a_n = (2.0/periodoL)*simps(array_Y*np.cos(2.*np.pi*contadorN*array_X/periodoL), array_X)
    
    b_n = (2.0/periodoL)*simps(array_Y*np.sin(2.*np.pi*contadorN*array_X/periodoL), array_X)

    return a_n, b_n


#================================================================
# Parámetros
periodoL = 4 # Periodicity of the periodic function f(x)
freq = 4 # No of waves in time period L
dutycycle = 0.5
width_range = 1
nMuestras = 1000 #No of terms for the function
nTerminos = 25 #No of terms in the Fourier Transform 


# Puntos t
arreglo_X = np.linspace(0, periodoL, nMuestras, endpoint=False)

# Señales y(t)
arreglo_Y = signal.sawtooth(2.0*np.pi*arreglo_X*freq/periodoL ,width=width_range)

# arreglo_Y = signal.square(2.0*np.pi*arreglo_X*freq/periodoL , duty=dutycycle)
# arreglo_Y = signal.gausspulse(2.0*np.pi*arreglo_X*freq/periodoL, fc=0.05)

señal_aprox = Analisis_Fourier(arreglo_X, arreglo_Y, nTerminos)

# Gráfico
fig, ax = plt.subplots(dpi=120)
ax.plot(arreglo_X, señal_aprox, label='Aprox Series de Fourier')
ax.plot(arreglo_X, arreglo_Y, label='Señal original')
ax.set_xlabel('$t$')
ax.set_ylabel('$y=f(t)$')
plt.legend(loc='best', prop={'size':10})
plt.title('Análisis de Fourier para una señal')
plt.show()
