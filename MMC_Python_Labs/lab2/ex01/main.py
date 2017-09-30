import numpy as np
from sympy import *

g_verbose = True

def		myFunction(x):
	return x ** (1.0 / 2) - np.e ** (-x)

def		bisectionMethod(xMin, xMax, tolerance, f):
	if f(xMin) > 0 or f(xMax) < 0:
		raise Exception('Invalid limits')

	iterations = 0

	x = (xMin + xMax) / 2
	while np.fabs(f(x)) > tolerance:
		iterations += 1

		x = (xMin + xMax) / 2
		if f(x) < 0:
			xMin = x
		else:
			xMax = x

	if g_verbose:
		print("BisectionMethod iterations: %d" % (iterations))

	return x

def		newtonMethod(x0, tolerance, f):
	xSymbol = Symbol('x')
	derivatedF = lambdify(xSymbol, f(xSymbol).diff(xSymbol), 'numpy')

	iterations = 0
	x = x0
	while np.fabs(f(x)) > tolerance:
		iterations += 1

		x = x - f(x) / derivatedF(x)

	if g_verbose:
		print("NewtonMethod iterations: %d" % (iterations))

	return x

#Source: http://www.sciencedirect.com/science/article/pii/S0893965913002930
def		simplifiedNewtonMethod(xMin, xMax, tolerance, f):
	xSymbol = Symbol('x')
	derivatedF = lambdify(xSymbol, f(xSymbol).diff(xSymbol), 'numpy')

	x0 = (xMin + xMax) / 2
	xStar = x0
	x = x0 - f(x0) / derivatedF(x0)
	
	xPrev = x
	xStarPrev = xStar

	while np.fabs(f(x)) > tolerance:
		x = x - f(x) / derivatedF(1/2 * (x + xStar))
		tmp = xStar

		print f(x)

		xStar = x - f(x) / derivatedF(1/2 * (xPrev + xStarPrev))
		
		xPrev = x
		xStarPrev = tmp

	return x	

def		secantMethod(x0, x1, tolerance, f):
	iterations = 0
	x = x1
	while np.fabs(x) > tolerance:
		if f(x1) - f(x0) == 0:
			break

		iterations += 1

		x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

		x0 = x1
		x1 = x

	if g_verbose:
		print("SecantMethod iterations: %d" % (iterations))

	return x


tolerance = 10.0 ** -14

print bisectionMethod(0, 1.2, tolerance, myFunction)
print newtonMethod(0.6, tolerance, myFunction)
# print simplifiedNewtonMethod(0.6, 1.2, tolerance, myFunction)
print secantMethod(0.6, 1, tolerance, myFunction)