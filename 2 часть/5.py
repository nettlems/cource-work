from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(1, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

Average_line = A.mean(axis=1)
Average_column = A.mean(axis=0)
Average_line = Average_line[: , np.newaxis]
A = np.hstack((A, Average_line))
Average_column = np.hstack((Average_column, [0.]))
A = np.vstack((A, Average_column))

print("Новая матрица:\r\n{}\n".format(A))