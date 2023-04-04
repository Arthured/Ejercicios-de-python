# import numpy as np
import math


def print_matrix(A):
    for row in A:
        for entry in row:
            print("\t{:.3f}".format(entry), end="")
        print()
    print()


# epsd=np.finfo(np.float64).eps
epsd = 2.2 * 10 ** (-16)
# A=[[3,2,5,6,7,10],[5,3,8,10,4,15],[4,2,6,8,2,12],[2,3,5,4,7,10]]
# A=[[2,3,-1,10],[4,-1,3,-1],[-3,0,-7,4]]
A = [[1, 2, 3, 1], [4, 5, 6, -2], [7, 8, 10, 5]]
print_matrix(A)
m = len(A)  # numero de filas/renglones
n = len(A[0])  # numero de columnas
k = 0
col = 0
f = 0
while k < m:
    position = k
    # Localiza el elemento mas grande en la columna col en los renglones del k a m;
    # sea pos la posicion del mas grande en este rango
    for i in range(k, m):
        if A[position][col] < A[i][col]:
            position = i
    # print(position)
    # Intercambia renglones k y pos
    if k < m - 2:
        A[k], A[position] = A[position], A[k]
        #print_matrix(A)
    # Si math.fabs(A[k][col])>epsd, haz la eliminacion gaussiana,
    # o decrementa k en caso anterior (sigue en el mismo renglon)
    if math.fabs(A[k][col]) > epsd:
        m1 = k + 1
        n1 = col
        a = A[k][col]  # asigna a a el valor de la entrada pivote
        b = 1
        while m1 < m:
            if A[m1][col] != 0:
                b = a / A[m1][col]  # agarramos el valor para que sea igual al pivote y dividir
            while n1 < n:
                A[m1][n1] = A[k][n1] - b * A[m1][n1]
                if math.fabs(A[m1][n1]) < epsd:
                    A[m1][n1] = 0
                n1 += 1
                f += 1
                # print(n1)
            n1 = col
            m1 += 1
    k += 1
    col += 1  # incrementa en 1 tanto col como k
for i in range(0,m):
    a=A[i][i]
    for j in range(0,n):
        if a!=0:
            if A[i][j]!=0:
                A[i][j]=A[i][j]/a

print_matrix(A)
print(A)
