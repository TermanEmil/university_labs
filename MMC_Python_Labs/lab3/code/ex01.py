import numpy as np

def f1(x):
	return 2 * np.e**(-x)

def f2(x):
	return 0.9 / (1 + x**4)

def f3(x):
	return 6.28 + np.sin(x)

# Find an x in which f(x) is almost x.
def fixed_point_finder(f, x0, tolerance, max_iters = 1000, verbose = False):
	iterations = 0
	x = x0

	while np.fabs(x - f(x)) > tolerance and iterations < max_iters:
		x = f(x)
		iterations += 1
		if verbose:
			print("\t%3d) x = %.20f |x - f(x)| = %.20f" % \
				(iterations, x, np.fabs(x - f(x))))

	return x, iterations

# Find an x in which f(x) is almost x, using Aitken extrapolation.
# It finds the solution much much faster.
def aitken_extrapolation(f, x0, tolerance, max_iters = 1000, verbose = False):
	iterations = 0
	x1, x2, x3 = x0, x0, x0

	while True:
		x0 = x1
		x1 = f(x0)
		x2 = f(x1)
		lambda_n = (x2 - x1) / (x1 - x0)
		x3 = x2 + lambda_n / (1 - lambda_n) * (x2 - x1)
		x1 = x3
		iterations += 1

		if verbose:
			print("\t%3d) x0 = %.20f |x3 - x2| = %.20f" % \
				(iterations, x0, np.fabs(x3 - x2)))

		if np.fabs(x3 - x2) < tolerance or iterations > max_iters:
				break

	return x1, iterations

def print_result(method, f, x, iterations):
	print("[%s] %s: x = %.5f |x - f(x)| = %.5f; iterations = %d" % \
		(method, f.__name__, x, np.fabs(x - f(x)), iterations))

tolerance = 10 ** -8
verbose = False

functions = [f1, f2, f3]
initialVals = [0.8, 0.75, 6]

for i in range(len(functions)):
	f, x0 = functions[i], initialVals[i]

	for alg in (fixed_point_finder, aitken_extrapolation):
		x, iterations = alg(f, x0, tolerance, verbose = verbose)
		print_result(alg.__name__, f, x, iterations)

	print("")