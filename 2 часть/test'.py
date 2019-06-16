from random import randint
import numpy as np
N, M = 5, 8
A = [[randint(1, 10) for j in range(M)] for i in range(N)]
A = np.array(A)
print(A)