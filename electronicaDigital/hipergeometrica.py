from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero para escoger una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

def recibirParametros():
    M=int(input("Ingrese el tamaño de la población: "))
    n=int(input("Ingrese el numero de individuos que cumplen la condicion: "))
    N=int(input("Ingrese el tamaño de la muestra: "))
    parametros = [M,n,N]
    return parametros


def distrbucionHipergeometrica():
    parametros = recibirParametros()
    rv = hypergeom(parametros[0],parametros[1],parametros[2])
    x = np.arange(0, parametros[1]+1)
    densidad=rv.pmf(x)
    print ("La densidad de frecuencia es de:  ",densidad)
    return densidad

def graficarDistribucion():
    parametros = recibirParametros()
    rv = hypergeom(parametros[0],parametros[1],parametros[2])
    x = np.arange(0, parametros[1]+1)
    densidad=rv.pmf(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, densidad, 'bo')
    ax.vlines(x, 0, densidad, lw=2)
    ax.set_xlabel('numero de elementos que presentan esta característica')
    ax.set_ylabel('Funcion de densidad')
    plt.show()

def calcularMedia():
    parametros = recibirParametros()
    rv = hypergeom(parametros[0],parametros[1],parametros[2])
    mean=rv.median
    print ("La media de la distribucion es de",mean)
    return mean

def calcularMediana():
    parametros = recibirParametros()
    rv = hypergeom(parametros[0],parametros[1],parametros[2])
    median=rv.median
    print ("La mediana de la distribucion es de",median)
    return median

def calcularVarianza():
    parametros = recibirParametros()
    rv = hypergeom(parametros[0],parametros[1],parametros[2])
    varianza=rv.var()
    print ("La varianza de la distribucion es de",varianza)
    return varianza


salir = False
opcion = 0
 
while not salir:
 
    print ("1. Calcular probabilidad usando la distribucion hipergeométrica")
    print ("2. Graficar distribucion hipergeometrica")
    print ("3. Calcular la probabilidad y mostrar la media ")
    print ("4. Calcular la probabilidad y mostrar la mediana")
    print ("5. Calcular la probabilidad y mostrar la varianza ")
    print ("6. Salir")
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()

    if opcion == 1:
        distrbucionHipergeometrica()
    elif opcion == 2:
        graficarDistribucion()
    elif opcion == 3:
        calcularMedia()
    elif opcion == 4:
        calcularMediana()
    elif opcion == 5:
        calcularVarianza()
    elif opcion == 6:   
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Fin")
