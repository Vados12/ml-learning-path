import numpy as np

# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y +2z = -3

A = np.array([[2, -3, -2], [1, -1, 1], [-1, 2, 2]])
AT = A.T
print("Матрица A:\n", AT)
B = np.array([8, -11, -3])
print("Матрица B:\n", B)

x = np.linalg.solve(AT, B)

Examination = AT @ x
if np.allclose(Examination, B):
    print("Ответ: ", x)
else:
    print("Error")


eigenvalues, eigenvectors = np.linalg.eig(AT)
detA = np.linalg.det(AT)
print("Детерминант матрицы A: \n", detA)
print("Собственные числа: \n",eigenvalues)
print("Собственные векторы: \n",eigenvectors)
