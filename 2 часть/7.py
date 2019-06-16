from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

Sum = A.sum()
print("Сумма элементов всей матрицы: " + str(Sum) + "\n")
Sum_column = A.sum(axis=1)
X = []
for i in range(0, N):
    n = Sum_column[i] / Sum
    X.append(n)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))

print(A)