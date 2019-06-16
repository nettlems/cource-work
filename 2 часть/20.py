from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))
b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))