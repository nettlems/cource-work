from random import randint
import numpy as np
L = np.random.randint(0, 3)
K = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

n = 0
for i in range(0, L):
    for j in range(0, M):
        if A[i,j] == 0:
            n += 1
print("Количество нулевых элементов в верхних L солбцах: {}\n".format(n))
m = 0
for i in range(0, K):
    for j in range(0, N):
        if A[j,i] == 0:
            m += 1
print("Количество нулевых элементов в левых L солбцах: {}\n".format(m))