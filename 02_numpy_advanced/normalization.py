import numpy as np

random_value = np.random.randint(0, 10, size=(10, 5))
print(random_value)

mean = np.mean(random_value, axis=0)
std = np.std(random_value, axis=0)

Z = (random_value - mean) / std
print(Z)
print(np.mean(Z, axis=0))
print(np.std(Z, axis=0))