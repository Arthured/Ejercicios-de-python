'''def imp(n):
    if n>=1:
        print(n)
        imp(n-1)
    elif n==0:
        return
    else:
        print("Valor incorrecto")
imp(5)'''
# def impuesto(precio, iva):
#     preciototal = precio*(1+iva/100)
#     return preciototal
# precio=float(input("Ingrese el precio: "))
# iva=float(input("ingrese el porcentaje de iva: "))
# print(f"el precio total es {impuesto(precio, iva)}")d
def faren(celsius):
    return ((9/5)*celsius + 32)
def cels(fahrenheit):
    return ((5/9)*(fahrenheit-32))
C=float(input("ingrese la temperatura en C°: "))
F=float(input("ingrese la temperatura en F°: "))
print(f"{C} C° son {faren(C)}F°")
print(f"{F} F° son {cels(F):.2f}C°")