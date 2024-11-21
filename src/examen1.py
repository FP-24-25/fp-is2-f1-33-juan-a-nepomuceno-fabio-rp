'''
Created on 24 oct 2024

@author: fabio
'''
from collections import Counter

def producto(n:int, k:int):
    i:int=1
    if (i < (k+1)) and (0<k<=n):
        resultado:int = 1
        for var in range(i,k-1):
            resultado *= (n-var+1)
    else:
        raise ValueError("Los parámetros introducidos son incorrectos")
    
    return(resultado)


def f_factorial(num:int):
    if (num==0):
        return(1)
    else:
        producto:int=1
        for i in range(1,num+1):
            producto*=i
        return(producto)
    
    
def combinatorio(n:int,k:int):
    if (n<=k) or (k<0):
        raise ValueError("Los parámetros introducidos son incorrectos")
    
    return f_factorial(n)/(f_factorial(k+1)*f_factorial(n-(k+1)))


def s2(n:int,k:int):
    if(0<= k <=n):
        
        sumatorio:float=0
        for i in range(k+1):
            sumatorio += (   ((-1)**i) * combinatorio(k, i) * ((k-i)**(n+1))  )
        
        resultado:float = (f_factorial(k)/(n*f_factorial(k+2)))*sumatorio
        
    
    else:
        raise ValueError("Los parámetros introducidos son incorrectos")

    return(resultado)


def palabrasMasComunes(fichero:str = "fichero.txt", n:int = 5):
    if (n>1):
        try:
            with open(fichero,mode="r",encoding="utf-8",newline="") as archivo:
                contenido:str = archivo.read()
            
            splitted:list[str] = contenido.split("\n")
            contenido = ""
            for i in splitted:
                contenido += (i+" ")
            splitted:list[str] = contenido.split(" ")
            postCounter = Counter(splitted)
            resultado:list = []
            for i in postCounter:
                resultado.append((i,postCounter[i]))
            resultado.sort(key=lambda x: x[1])
            
            for i in range(len(resultado)-n):
                resultado.pop(0)
            
            return resultado
        
        except:
            raise ValueError("El nombre del archivo es incorrectos o no se puede leer")


    else:
        raise ValueError("n es menor o igual a 1")

    
    
try:
    print(producto(5,7))
except Exception as e:
    print(e)

try:
    print(producto(5,-1))
except Exception as e:
    print (e)

try:
    print(combinatorio(5,7))
except Exception as e:
    print (e)

try:
    print(combinatorio(6,-7))
except Exception as e:
    print (e)



try:
    print(s2(5,8))
except Exception as e:
    print (e)

try:
    print(s2(3,-8))
except Exception as e:
    print (e)
    
try:
    print(palabrasMasComunes("noexisteestenombre.txt",7))
except Exception as e:
    print (e)
    
try:
    print(palabrasMasComunes("fichero.txt",1))
except Exception as e:
    print (e)
    
    
try:
    print(combinatorio(6,10))
except Exception as e:
    print (e)
try:
    print(palabrasMasComunes("fichero.txt"))
except Exception as e:
    print (e)

