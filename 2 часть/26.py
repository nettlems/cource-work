from random import randint
import numpy as np
L = np.random.randint(0, 3)
K = np.random.randint(0, 3)
N, M = 8, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]

A = np.array(A)
print("Матрица:\r\n{}".format(A))

x = A[0:L ,0:K]
x_sum = x.mean()
print("Вверхняя левая часть: среднее арифметическое = " + str(x_sum) + "\n" + str(x))
y = A[L: ,0 :K]
y_sum = y.mean()
print("\nНижняя левая часть: среднее арифметическое = " + str(y_sum) + "\n" + str(y))
z = A[0:L ,K:]
z_sum = z.mean()
print("\nВверхняя правая часть: среднее арифметическое = " + str(z_sum) + "\n" + str(z))
a = A[L: ,K:]
a_sum = a.mean()
print("\nНижняя правая часть: среднее арифметическое = " + str(a_sum) + "\n" + str(a))