import numpy as np

def f1(x):
	return 2 * np.e**(-x)

def f2(x):
	return 0.9 / (1 + x**4)

def f3(x):
	return 6.28 + np.sin(x)

def fixedPointFinder(f, x0, tolerance, maxIters = 1000, verbose = False):
	iterations = 0
	x = x0
	while np.fabs(x - f(x)) > tolerance and iterations < maxIters:
		x = f(x)
		iterations += 1
		if verbose:
			print("\t%3d) x = %.20f |x - f(x)| = %.20f" % \
				(iterations, x, np.fabs(x - f(x))))
	return x

def printResult(f, x):
	print("%s: x = %.20f f(x) = %.20f |x - f(x)| = %.20f" % \
		(f.__name__, x, f(x), np.fabs(x - f(x))))

tolerance = 10 ** -6
verbose = False

functions = [f1, f2, f3]
initialVals = [0.8, 0.75, 6]

for i in range(len(functions)):
	f, x0 = functions[i], initialVals[i]
	result = fixedPointFinder(f, x0, tolerance, verbose = verbose)
	printResult(f, result)
