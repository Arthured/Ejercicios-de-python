import sympy
import  math
x = sympy.symbols('x')#etiqueta al caracter que va a ser la variable
expr = input("Ingrese la ecuacion: ")
n=int(input("¿cuantos puntos tienes?  "))#ingresas todos los puntos
lista=[]
for i in range(n):
    a=float(input("ingrese el valor de x:"))
    b = float(input("ingrese el valor de y:"))
    punto=[a,b]
    lista.append(punto)

#n=8
c=0
#lista=[[-1,10],[0,9],[1,7],[2,5],[3,4],[4,3],[5,0],[6,-1]]
print(lista[2][1])
i=0
maximo=[]
b=0
for i in range (n):#evalua cada punto x en la ecuacion dada y empieza a sacar los valores necesarios para calcular el error
    h=sympy.sympify(expr).subs(x,lista[i][0])
    a=abs(lista[i][1]-h)
    maximo.append(a)#error maximo
    b=b+a#error medio
    c=c+a**2#error cuadratico medio
b1=(1/n)*b
c1=math.sqrt((1/n)*c)
print(f"El error maximo es :{max(maximo)}")
print(f"El error medio es {b1}")
print(f"El error cuadratico medio es {c1}")

