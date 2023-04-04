import sympy#Debes instalar la libreria sympy
import math
x = sympy.symbols('x')#etiqueta al caracter que va a ser la variable
"""n=int(input("¿cuantos puntos tienes?  "))#ingresas todos los puntos
lista=[]
for i in range(n):
    a=float(input("ingrese el valor de x:"))
    b = float(input("ingrese el valor de y:"))
    punto=[a,b]
    lista.append(punto)"""
n=5
lista=[[.2,.1960],[.4,.7859],[.6,1.7665],[.8,3.14],[1,4.9075]]
a=0
b=0
c=0
e=0
for i in range(n):
    a=a+(lista[i][0])**2
    b=b+lista[i][0]
    c=c+(lista[i][0]*lista[i][1])
    e=e+lista[i][1]
A=(e*b-c*n)/(b**2-n*a)
B=(b*c-e*a)/(b**2-n*a)
if B<0:
    print(f"y={A}x {B}")
else:
    print(f"y={A}*x+{B}")
a1=str(A)
b1=str(B)

y=(a1 +'*'+'x'+ '+' + b1)

print(y)
c=0
i=0
maximo=[]
b=0
for i in range (n):#evalua cada punto x en la ecuacion dada y empieza a sacar los valores necesarios para calcular el error
    h=sympy.sympify(y).subs(x,lista[i][0])
    a=abs(lista[i][1]-h)
    maximo.append(a)#error maximo
    b=b+a#error medio
    c=c+a**2#error cuadratico medio
b1=(1/n)*b
c1=math.sqrt((1/n)*c)
print(f"El error maximo es :{max(maximo)}")
print(f"El error medio es {b1}")
print(f"El error cuadratico medio es {c1}")
#y=A*x+B
#Hace una aproximacion con regrecion de grado m
m=int(input("Ingrese el grado de la ecuacion: "))
a1=0
a2=0
for i in range(n):
    a1=a1+(lista[i][0]**m)*lista[i][1]
    a2=a2+lista[i][0]**(2*m)
A1=a1/a2
a3=str(A1)
print("y= "+a3+' x^'+str(m))