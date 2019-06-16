from random import randint
import numpy as np
L = np.random.randint(0, 3)
K = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))
x = A[0:L ,0:K]
x_sum = x.sum()
print("Вверхняя левая часть: сумма равна = " + str(x_sum) + "\n" + str(x))
y = A[L: ,0 :K]
y_sum = y.sum()
print("\nНижняя левая часть: сумма равна = " + str(y_sum) + "\n" + str(y))
z = A[0:L ,K:]
z_sum = z.sum()
print("\nВверхняя правая часть: сумма равна = " + str(z_sum) + "\n" + str(z))
a = A[L: ,K:]
a_sum = a.sum()
print("\nНижняя правая часть: сумма равна = " + str(a_sum) + "\n" + str(a))