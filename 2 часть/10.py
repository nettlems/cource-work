from random import randint
import numpy as np
K = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

K_arr = np.array(A[:, K-1])
K_arr = K_arr[: , np.newaxis]
print("K-ый столбец: \r\n{}\n".format(K_arr))
A = A * K_arr

print("Новая матрица:\r\n{}\n".format(A))