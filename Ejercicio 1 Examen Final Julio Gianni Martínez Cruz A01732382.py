#Ejercicio 1 Examen Final
#Julio Gianni Martínez Cruz A01732382

import math

def f(x):
    f = 1 / ((x**2) + (1/10))
    return f 

def simpson38(a,b):
    h= (b-a)/3
    I = (3*h/8)*(f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))
    return I

def main():
    a = int(input("Introduzca límite inferior de la integración: "))
    b = int(input("Introduzca límite superior de la integración: "))
    I= simpson38(a,b)
    print("Valor de la integración numérica por Simpson 3/8: ",I)
    
main()
