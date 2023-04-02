a=input('Ingrese la primera palabra:')
b=input('Ingrese la segunda palabra:')
a=a.lower()
b=b.lower()
a=list(a)
b=list(b)
a.sort()
b.sort()
if a==b:
    print('Es un anagrama')
else:
    print('No es un anagrama')
