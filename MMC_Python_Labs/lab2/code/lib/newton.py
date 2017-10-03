from myUtils import _printResults
import numpy as np
from sympy import *

def		newtonMethod(x0, tolerance, f, verbose = True):
	if verbose: print("Newton Method:")

	xSymbol = Symbol('x')
	derivatedF = lambdify(xSymbol, f(xSymbol).diff(xSymbol), 'numpy')

	iterations = 0
	pData = []
	x = x0
	while np.fabs(f(x)) > tolerance:
		pData += [[iterations, x]]

		iterations += 1
		x = x - f(x) / derivatedF(x)

	pData += [[iterations, x]]
	if verbose: _printResults(iterations, x)
	return (x, pData)
