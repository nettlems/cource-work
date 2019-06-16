from random import randint
import numpy as np
N, M = 8, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

B = (A + A.T)/2
print("Новая матрица:\r\n{}\n".format(B))