import numpy as np
from numpy.random import rand

random_mark = np.random.randint(1, 6, size=(4, 5))


print("Оценки:\n", random_mark)

print("Ср. значение по столбцам:\n", np.mean(random_mark, axis=0))
print("Ср. значение по строкам:\n", np.mean(random_mark, axis=1))
print("Максимальная:\n", np.max(random_mark))
print("Минимальная:\n", np.min(random_mark))

random_mark = random_mark + 1
random_mark = np.clip(random_mark, 2, 5)
print("Измененная матрица оценок:\n",random_mark)

