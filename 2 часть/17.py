from random import randint
import numpy as np
L = np.random.randint(0, 3)
N, M = 5, 8
A = [[randint(-10, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print("Матрица:\r\n{}".format(A))

a = np.random.randint(0, 10, M)
print("Допонлительная строка: " + str(a))
print("\n L = " + str(L))

row = np.random.randint(low=-9, high=10, size=M)
print("Строка для вставки: {}".format(row))
A = np.insert(A, L, row, axis=0)

print("Новая матрица:\r\n{}\n".format(A))