from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

Max = A.max(axis=1)
Max = np.array(Max)[: , np.newaxis]
A = A / Max

print("Новая матрица:\r\n{}\n".format(A))