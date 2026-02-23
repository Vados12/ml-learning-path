import numpy as np

# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y +2z = -3

A = np.array([[2, -3, -2], [1, -1, 1], [-1, 2, 2]])
print("Матрица A:\n", A)
B = np.array([8, -11, -3])
print("Матрица B:\n", B)

x = np.linalg.solve(A, B)
print("x = ", x)
