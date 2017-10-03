from myUtils import _printResults
import numpy as np
from sympy import *

def		bisectionMethod(xMin, xMax, tolerance, f, verbose = True):
	if verbose: print "Bisection Method:"

	if f(xMin) > 0 or f(xMax) < 0:
		raise Exception('Invalid limits')

	iterations = 0
	pData = []

	x = xMin
	while np.fabs(f(x)) > tolerance:
		#plot stuff
		pData += [[iterations, x]]
		iterations += 1

		x = (xMin + xMax) / 2
		if f(x) < 0:
			xMin = x
		else:
			xMax = x

	pData += [[iterations, x]]

	if verbose: _printResults(iterations, x)
	return (x, pData)