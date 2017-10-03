import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def		myFunction(x):
	return x * (float(c) - 1 - float(c) * x)

def		getSol(c):
	x = Symbol('x')
	sol = solve(x * (float(c) - 1 - float(c) * x), x)

	return sol[-1]

def		newtonMethod(x0, tolerance, f, maxIterations = 100):
	xSymbol = Symbol('x')
	derivatedF = lambdify(xSymbol, f(xSymbol).diff(xSymbol), 'numpy')

	iterations = 0
	x = x0
	while np.fabs(f(x)) > tolerance:
		iterations += 1

		xPrev = x
		x = x - f(x) / derivatedF(x)
		if iterations >= maxIterations:
			break

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

tolerance = 10 ** -14

iterationsList = []
cValues = np.linspace(0, 100, 100)

for c in cValues:
	solution = getSol(c)

	#Newton
	title = "Newton"
	(x, iterations) = newtonMethod(1.0, tolerance, myFunction)
	print("Newton: c = %- 5.5f; iterations = %- 3d; solution = % -5.5f |"
		" %- 5.5f; diff = %-5.5f" % (c, iterations, x, solution, solution - x))
	
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

plt.show()