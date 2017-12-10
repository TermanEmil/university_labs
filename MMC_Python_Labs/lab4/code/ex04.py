import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):
	L = np.tril(A)
	U = A - L
	for i in range(n):
		x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
	return x

A = np.array([
	[1.0, -2.0],
	[2.0, 1.0]])

b = [-1.0, 3.0]
x = [0, 0]

print("Last iteration: ", gauss(A, b, x, 20))
print("Solution:\t", solve(A, b))