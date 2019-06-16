from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(1, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

Average = A.mean(axis=1)
index = Average.argmax(axis=0)
max = Average.max(axis=0)

print("Наибольшее среднее значение: {}".format(max))