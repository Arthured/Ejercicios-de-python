from main import print_hi
print_hi("Arturo")
import random
c=0
a=0
ayuda=0
contar=0
z=0
datos=[]
while z<100:
    while c<1000:
        bandera = 0
        lista=[]
        for i in range(50):
            lista.append(random.randrange(1,366))
    #print(lista)
        pivote = lista
        for x in lista:
            pivote.remove(x)
            for y in pivote:
                if x==y:
                    contar += 1
                    bandera=1
                    break
            if bandera==1:
                break
        c+=1
        a+=1

    ayuda+=contar
    c=0
    datos.append(contar/1000)
    contar=0
    z+=1
print(datos)
print(ayuda/a,ayuda,a)
