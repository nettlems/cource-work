from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

X = []
for i in range(0, N):
    K = 0
    for j in range(0, M):
        if A[i,j] < 0:
            K += 1
    X.append(K)
Y = []
for i in range(0, M):
    K = 0
    for j in range(0, N):
        if A[j,i] < 0:
            K += 1
    Y.append(K)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))
Y = np.hstack((Y, [0.]))
A = np.vstack((A, Y))

print("Новая матрица:\r\n{}\n".format(A))