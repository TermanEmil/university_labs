from MyLib import *

def		myFunction(x):
	return x * (np.float(c) - 1 - np.float(c) * x)

def		derivatedF(x):
	return np.float(c) - 1 - 2 * x * np.float(c)

tolerance = 10.0 ** -16
verbose = True
initialGuess = 1.0
derivF = derivatedF

# for c in np.linspace(60, 70, 1000):
c = 69.35935935935935958696
sol = 1.0 - 1.0 / c
(x, xVals) = newton(initialGuess, tolerance, myFunction,
	derivF = derivF, sol = sol, verbose = verbose)
print("c = %.20f x = %.20f iterations = %d" % (c, x, len(xVals)))

