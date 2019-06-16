from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

Sum = A.sum()
B=np.sum(A)
M_sum = np.sum(A, axis=0)/np.sum(A)
A = np.vstack((A,M_sum))
print("Новая матрица:\r\n{}\n".format(A))

