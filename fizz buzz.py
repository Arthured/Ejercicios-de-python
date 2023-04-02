a = int(input("Ingrese el numero fizz:"))
b = int(input("Ingrese el numero buzz:"))

for i in range(1, 100):
    if i % a == 0 and i % b != 0:
        print('fizz', end='   ')
    elif i % b == 0 and i % a != 0:
        print('buzz', end='   ')
    elif i % a == 0 and i % b == 0:
        print('fizz buzz', end='   ')
    else:
        print(f'{i}', end='   ')
    if i % 10 == 0:
        print('\n')