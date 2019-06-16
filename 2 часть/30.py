from random import randint
import numpy as np

K = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

M_n = np.sum(A, axis=0) * (-1)
A = np.vstack((A, M_n))

print("Новая матрица:\r\n{}\n".format(A))