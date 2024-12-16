import numpy as np

A = np.array([[94, 34], [22, 67]])
y = np.array([8400, 5400])
print(A, y)
print(np.linalg.solve(A.T, y))