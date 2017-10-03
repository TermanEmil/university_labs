from myUtils import _printResults
import numpy as np
from sympy import *

def		secantMethod(x0, x1, tolerance, f, verbose = True):
	if verbose: print "Secant Method"

	iterations = 0
	pData = [[0, x0]]
	x = x1
	while np.fabs(f(x)) > tolerance:
		if f(x1) - f(x0) == 0:
			break
		
		x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

		x0 = x1
		x1 = x
		
		#Plot stuff
		iterations += 1
		pData += [[iterations, x]]

	pData += [[iterations, x]]
	if verbose: _printResults(iterations, x)
	return (x, pData)
