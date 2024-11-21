import src.lecturas.lecturas as rd

print("\n\nTEST DE LA FUNCIÓN 6:")
nombre:str = "lin_quijote"
sep = " "
palabra:str = "datos"
print("El número de veces que aparece la palabra ", palabra, " en el fichero ", nombre, ".txt es: ",
    rd.contadorPalabras(nombre, sep, palabra),sep=""
    )


print("\n\nTEST DE LA FUNCIÓN 7:")
nombre:str = "lin_quijote"
cadena:str = "de la Mancha"
print("Las líneas en las que aparece la palabra ", cadena, " en el fichero ", nombre, ".txt son:\n",
    rd.contadorLineas(nombre, cadena),sep=""
    )


print("\n\nTEST DE LA FUNCIÓN 8:")
nombre:str = "archivo_palabras"
sep:str = " "
print("Las palabras únicas en el fichero ", nombre, ".txt son:\n",
    rd.recuentoPalabras(nombre, sep),"\n",sep=""
    )


print("\n\nTEST DE LA FUNCIÓN 9:")
nombre:str = "palabras_random"
print("La longitud promedio de las líneas del fichero ", nombre, ".csv es: ",
    rd.longitud_promedio_lineas(nombre),"\n",sep=""
    )

nombre:str = "vacio"
print("La longitud promedio de las líneas del fichero ", nombre, ".csv es: ",
    rd.longitud_promedio_lineas(nombre),sep=""
    )

