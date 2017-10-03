from myUtils import _printResults
import numpy as np
from sympy import *

def		simplifiedNewtonMethod(x0, tolerance, f, verbose = True):
	if verbose: print "Simplified Newton Method"

	iterations = 0
	pData = []
	x = x0
	while np.fabs(f(x)) > tolerance:
		#plot stuff
		pData += [[iterations, x]]
		iterations += 1

		fOfX = f(x)
		x = x - (fOfX ** 2) / (f(x + fOfX) - fOfX)

	pData += [[iterations, x]]
	if verbose: _printResults(iterations, x)

	return (x, pData)
