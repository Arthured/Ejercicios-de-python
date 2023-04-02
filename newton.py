'''print("Hola mundo")
i = input("Hola ")
print (i)
import  numpy as np 
fx = lambda x :input("ingrese funcion: ")
dx = lambda x:input("ingresesuderivada: ")
lista = []
x0=int(input("ingrese primer valor: "))
for i in range(100):
    if i == 0 and dx(x0) != 0:
        lista.append(x0-fx(x0)/dx(x0))
'''
import math 

x0 = float (input ("Ingrese el numero al que se le desea sacar raiz: "))
x1= float (input("Ingrese un aproximado: "))
lista = [x0,x1]
for i in range(100):
    a=(1/2)*(lista[1+i]+lista[0]/lista[i+1])
    lista.append(a)
    if lista[i]==math.sqrt(x0):
        break;
print (lista)
print (math.sqrt(x0))
