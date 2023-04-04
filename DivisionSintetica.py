def factores(a):#La funcion consige todos los factores del numero a
    factor=[]
    if a!=1:
        for i in range(abs(a)):
            if a%(i+1)==0:
                factor.append(int(i+1))
                factor.append(int(-i-1))
            if abs(a)**(1/2)<(i+1) and factor == []:
                return [1,-1,a,-a]
        return(factor)
    else:
        return [-1,1]
def elim_repetidos(lista):#elimina todos los elementos repetidos de una lista
    lista_sin=[]
    for i in lista:
        if i not in lista_sin:
            lista_sin.append(i)
    return lista_sin

n=int(input("Ingresa el grado de la ecuacion"))
lista=[]
for i in range(n+1):
    c=int(input(f"Ingresa el valor de c_{i}"))
    lista.append(c)
# coeficientes=map(lambda n:n/lista[0],lista)
# lista=list(coeficientes)
# print(lista)
print(lista)
cn=factores(lista[0])
c0=factores(lista[n])
print(c0,cn)
pos_raiz=[]

for ele in cn:
    pos_raiz=pos_raiz + list(map(lambda n:n/ele,c0))
pos_raiz=elim_repetidos(pos_raiz)
print(pos_raiz)
solucion=[]
raices=[]
a=0
for raiz in pos_raiz:
    division = []
    division.append(lista[0])
    for x0 in range(1,n+1):
        a=division[x0-1]*raiz+lista[x0]
        division.append(a)
    print("Hola")
    if division[n]==0:
        division.pop(n)
        solucion.append(division)
        print(solucion)
        raices.append(raiz)
    print(division)
print(raices)
print(solucion)