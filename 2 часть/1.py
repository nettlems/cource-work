from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(1, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
index = sum.argmax(axis=0)
max = A.max(axis=0)
max = max[index]

print("Наибольшее значение: {}".format(max))