from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

bool = A == 0
col = np.sum(bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)
print("Новая матрица:\r\n{}\n".format(A))