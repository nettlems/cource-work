from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

iu = np.triu_indices(N, 1)
a = A[iu]
a = np.sum(np.array(a))
print("\nCумма элементов выше главной диагонали = " + str(a))
b = np.fliplr(A)[iu]
b = np.prod(np.array(b))
print("\nПроизведение элементов выше побочной диагонали = " + str(b))