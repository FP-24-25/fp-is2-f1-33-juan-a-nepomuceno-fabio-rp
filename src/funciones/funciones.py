import math
def productoSecuencia(n:int,k:int):
    if (n>k):

        producto:int = 1
        
        for i in range(k):
            producto*= (n-i+1)
        
        return(producto)
    
    else:
        raise ValueError("n debe de ser mayor que k, vuelva a ingresar los datos.")

        
def productoGeométrico(a1:float, r:float, n:int):
    a:list[int] = [a1]
    for i in range(2,n+1):
        a.append(a[i-2]*r**(n-1))
    value:int = 1
    for j in a:
        value *= j
    
    return (value)

def f_factorial(num:int):
    if (num==0):
        return(1)
    else:
        producto:int=1
        for i in range(1,num+1):
            producto*=i
        return(producto)

def combinatorio(n:int,k:int):
    if (n<k):
        raise ValueError("El número total de elementos no puede ser menor al conjunto.")
    
    return f_factorial(n)/(f_factorial(k)*f_factorial(n-k))


def funcionS(n:int,k:int):
    if (n<k):
        raise ValueError("n debe ser mayor o igual a k.")
    
    sumatorio:int = 0
    for i in range(k):
        sumatorio += ((-1)**i)*combinatorio(k+1, i+1)*((k-i)**n)
    
    return(sumatorio/f_factorial(k))


def newton(f, df, x:float, err:float):
    while (abs(f(x))>err):
        x = x-(f(x)/df(x))
        
    return (x)












