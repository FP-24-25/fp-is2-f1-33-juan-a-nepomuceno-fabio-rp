from collections import Counter
from operator import __contains__
from typing import Optional

def contadorPalabras(nombre:str, sep:str, palabra:str) -> int:
    with open(nombre+".txt",mode="r",encoding="utf-8",newline="") as archivo:
        contenido:str = archivo.read()
        archivo.close()
    
    splitted:list[str] = contenido.split("\n")
    contenido = ""
    for i in splitted:
        contenido += (i+sep)
    splitted:list[str] = contenido.split(sep)
    postCounter = Counter(splitted)
    
    return postCounter[palabra]


def contadorLineas(nombre:str, cadena:str) -> list[str]:
    with open(nombre+".txt",mode="r",encoding="utf-8",newline="") as archivo:
        contenido:str = archivo.read()
        archivo.close()
        
    lineas:list[str] = contenido.split("\n")
    for i in reversed(range(len(lineas))):
        if (lineas[i].__contains__(cadena)):
            continue
        else:
            lineas.pop(i)
    return(lineas)
    

def recuentoPalabras(nombre:str, sep:str) -> list[str]:
    with open(nombre+".txt",mode="r",encoding="utf-8",newline="") as archivo:
        contenido:str = archivo.read()
        archivo.close()
    
    palabras:list[str] = []
    for line in contenido.split("\n"):
        for word in (line.split(sep)):
            palabras.append(word)
    postCounter = Counter(palabras)
    
    listaPalabras:list[str] = []
    for i in postCounter:
        listaPalabras.append(i)
    
    return (listaPalabras)



def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    from csv import reader as csvread
    
    with open(file_path+".csv",mode="r",encoding="utf-8",newline="") as archivo:
        contenido = csvread(archivo)

        total_palabras:int = 0
        total_lineas:int = 0
        for line in contenido:
            total_palabras += len(line)
            total_lineas +=1

        if (total_lineas==0):
            return None
        else:
            return(total_palabras/total_lineas)
    
         
    
    
