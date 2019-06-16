from random import randint
import numpy as np
H = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

a = []
b = []
for i in range(M):
    if H in A[:, i]:
        a.append(i+1)
    else:
        b.append(i+1)
print("Столбцы, которые имеют хотя бы одно число H - {}\n".format(a))
print("Столбцы, которые не имеют это число - {}\n".format(b))