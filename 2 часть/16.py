from random import randint
import numpy as np
L = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

print("L = " + str(L))
A = np.delete(A, (L-1), axis=0)

print("Новая матрица:\r\n{}\n".format(A))