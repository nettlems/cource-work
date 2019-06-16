from random import randint
import numpy as np
L = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

L_arr = np.array(A[L-1, :])
print("L страка: \r\n{}\n".format(L_arr))
A = A + L_arr

print("Новая матрица:\r\n{}\n".format(A))