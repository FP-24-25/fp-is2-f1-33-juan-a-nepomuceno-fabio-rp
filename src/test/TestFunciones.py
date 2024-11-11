import src.funciones.funciones as fn


###TEST DE FUNCIONES

print("\n\nTEST DE LA FUNCIÓN 1:")
#PARAMETROS
n1:int = 4
k1:int = 2
print(
    "El producto de ", n1, " y ", k1, " es: ",
    fn.productoSecuencia(n1, k1),sep=""
    )


print("\n\nTEST DE LA FUNCIÓN 2:")
#PARAMETROS
a1:int = 3
r:int = 5
k2:int = 2
print(
    "El producto de la secuencia geométrica con a1=", a1, ", r=", r,", y k=",k2," es: ",
    fn.productoGeométrico(a1, r, k2),sep=""
    )


print("\n\nTEST DE LA FUNCIÓN 3:")
#PARAMETROS
n3:int = 4
k3:int = 2
print(
    "El combinatorio de ", n3, " sobre ", k3, " es: ",
    fn.combinatorio(n3, k3)
    )


print("\n\nTEST DE LA FUNCIÓN 4:")
#PARAMETROS
n4:int = 4
k4:int = 2
print(
    "El valor de la función S(", n4, ",", k4, ") es: ",
    fn.funcionS(n4, k4)
    )


print("\n\nTEST DE LA FUNCIÓN 5:")
#PARAMETROS
f = lambda x: (2*(x**2))
df = lambda x: (4*x)
a5:float = 3
error:float = 0.001
print(
    "Para los siguientes valores de la función N.5:\n\tf(x)\n\tf'(x)\n\ta = ",a5,"\n\terror = ",error,"\n",
    "la primera aproximación de x tal que |f(x)| < error es: ",
    fn.newton(f,df,a5,error),
    sep="")



###FIN TEST FUNCIONES
