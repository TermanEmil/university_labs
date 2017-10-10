import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def		myFunction(x):
	return x * (np.float(c) - 1 - np.float(c) * x)

def		derivatedF(x):
	return np.float(c) - 1 - 2 * x * np.float(c)

def		getSol(c):
	x = Symbol('x')
	sol = solve(x * (float(c) - 1 - float(c) * x), x)

	return sol[-1]

def		newtonMethod(x0, tolerance, f, maxIterations = 100):
	# xSymbol = Symbol('x')
	# derivatedF = lambdify(xSymbol, f(xSymbol).diff(xSymbol), 'numpy')

	iterations = 0
	x = x0

	while True:
		iterations += 1

		xPrev = x
		x = x - f(x) / derivatedF(x)

		print(x)

		if np.fabs(x - xPrev) < tolerance:
			break

		# if iterations >= maxIterations:
		# 	break

	# while True:
	# # while np.fabs(f(x0)) > tolerance:
	# 	x1 = x0 - f(x0) / derivatedF(x0)

	# 	print("Polina loh: x0 = %.20f | x1 = %.20f" % (x0, x1))

	# 	iterations += 1

	# 	if np.fabs(x1 - x0) <= tolerance:
	# 		break
	# 	x0 = x1

	# 	if iterations > maxIterations:
	# 		break
		# x = x1

	return (x, iterations)

def		secantMethod(x0, x1, tolerance, f):
	iterations = 0
	x = x1
	while np.fabs(f(x)) > tolerance:
		if f(x1) - f(x0) == 0:
			break
		
		x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

		x0 = x1
		x1 = x
		iterations += 1

	return (x, iterations)

def		simplifiedNewtonMethod(x0, tolerance, f):
	iterations = 0
	pData = []
	x = x0
	while True:
		iterations += 1

		fOfX = f(x)
		xPrev = x
		x = x - (fOfX ** 2) / (f(x + fOfX) - fOfX)
		print(x)
		if np.fabs(x - xPrev) < tolerance:
			break

	return (x, iterations)

tolerance = (((10.0) ** (-16)))

iterationsList = []
cValues = np.linspace(np.float(50), np.float(70), 1000)

for c in cValues:
	solution = np.float(1.0) - 1.0/c

	#Newton
	title = "Newton"
	(x, iterations) = newtonMethod(100.0, tolerance, myFunction)
	print("Newton: c = %- 5.5f; iterations = %- 3d; solution = % -5.20f |"
		" %- 5.20f; diff = %-5.20f" % (c, iterations, x, solution, solution - x))

	#Simplified
	# title = "SimplifiedNewton"
	# (x, iterations) = simplifiedNewtonMethod(1.0, tolerance, myFunction)
	# print("SimplNewton: c = %- 5.5f; iterations = %- 3d; solution = % -5.5f |"
	# 	" %- 5.5f; diff = %-5.5f" % (c, iterations, x, solution, solution - x))
	
	#Secant
	# title = "Secant"
	# (x, iterations) = secantMethod(1, 1.01, tolerance, myFunction)
	# print("Bisection: c = %- 5.5f; iterations = %- 3d; solution = % -5.5f | %- 5.5f; diff = %-5.5f" %
	# 	(c, iterations, x, solution, solution - x))

	iterationsList.append(iterations)

print(iterationsList)

plt.title(title)
plt.xlabel("c")
plt.ylabel("Iterations")
plt.plot(cValues, iterationsList)

# plt.show()