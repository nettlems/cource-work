from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

a = np.diagonal(A)
a_sum = a.sum()
print("Главная диагональ: \n" + str(a) + "\n Её сумма = " + str(a_sum))
b = np.fliplr(A).diagonal(0)
b_sum = b.sum()
print("Побочная диагональ: \n" + str(b) + "\n Её сумма = " + str(b_sum))