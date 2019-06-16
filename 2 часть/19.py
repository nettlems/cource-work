from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))
a = np.diagonal(A, 1)
a_sum = a.sum()
print("Элементы которые выше главной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_sum))
b = np.diagonal(A, -1)
b_sum = b.sum()
print("Элементы которые ниже главной диагонали: \n" + str(b) + "\nИх сумма = " + str(a_sum))