import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def bisection(xL, xR, tolerance, f, sol = None, verbose = False):
	if verbose: print("Bisection")

	iters = 0
	xVals = [xL]

	while np.abs(xL - xR) > tolerance and np.sign(f(xL)) * np.sign(f(xR)) < 0:
		xMid = (xL + xR) / 2.0
		if f(xMid) < 0:
			xL = xMid
		else:
			xR = xMid
		xVals.append(xMid)
		iters += 1

		if verbose:
			print("\t%3d) xL = %.20f xR = %.20f" % (iters, xL, xR), end = '')
			if sol != None:
				print(" |x - x*| = %.20f" % np.fabs(xMid - sol))
			else:
				print("")

	if verbose: print("\t x = %.20f" % xMid)
	return (xMid, xVals)

def newton(x0, tolerance, f, derivF = None,
		maxIters = 100, sol = None, verbose = False):

	if verbose: print("Newton")

	if derivF == None:
		xSymbol = Symbol('x')
		derivFStr = f(xSymbol).diff(xSymbol)
		derivF = lambdify(xSymbol, derivFStr, 'numpy')

		if verbose: print("\tDerivF: %s" % (derivFStr))

	iters = 0
	xVals = [x0]

	while True:
		xNew = x0 - f(x0) / derivF(x0)

		if verbose:
			if iters >= maxIters:
				print("\t\033[5m%3d\033[0m", iters, end = '')
			else:
				print("\t%3d" % (iters), end = '')

			print(") x0 = %-5.20f xNew = %-5.20f" % (x0, xNew), end = '')
			if sol != None:
				print(" |xNew - x*| = %.20f" % np.fabs(xNew - sol))
			else:
				print("")

		if np.fabs(x0 - xNew) < tolerance:
			break

		if iters >= maxIters:
			break

		x0 = xNew
		xVals.append(x0)
		iters += 1

	if verbose: print("\t x = %.20f" % x0)
	return (x0, xVals)

def simplifNewton(x0, tolerance, f, maxIters = 100,
		sol = None, verbose = False):

	if verbose: print("Simplif Newton")

	iters = 0
	xVals = [x0]

	while True:
		if f(x0 + f(x0)) - f(x0) == 0: break

		xNew = x0 - (f(x0) ** 2) / (f(x0 + f(x0)) - f(x0))

		if verbose:
			if iters >= maxIters:
				print("\t\033[5m%3d\033[0m", iters, end = '')
			else:
				print("\t%3d" % (iters), end = '')

			print(") x0 = %-5.20f xNew = %-5.20f" % (x0, xNew), end = '')
			if sol != None:
				print(" |x0 - x*| = %.20f" % np.fabs(x0 - sol))
			else:
				print("")

		if np.fabs(x0 - xNew) < tolerance: break
		if iters >= maxIters: break

		x0 = xNew
		xVals.append(x0)
		iters += 1

	if verbose: print("\t x = %.20f" % x0)
	return (x0, xVals)

def secant(x0, x1, tolerance, f, sol = None, verbose = False):
	if verbose: print("Secant")

	iters = 0
	xVals = [x0]

	while np.fabs(x0 - x1) > tolerance:
		if f(x1) - f(x0) == 0: break

		xNew = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
		x0 = x1
		x1 = xNew

		if verbose:
			print("\t%3d) x0 = %-5.20f x1 = %-5.20f" % (iters, x0, x1), end='')
			if sol != None:
				print(" |xNew - x*| = %.20f" % np.fabs(xNew - sol))
			else:
				print("")

		xVals.append(xNew)
		iters += 1

	if verbose: print("\t x = %.20f" % xNew)
	return (xNew, xVals)

#Diagram utils for ex1
def plotDiagram(xVals, sol, label = None):
	x = range(0, len(xVals))
	y = [np.fabs(val - sol) for val in xVals]

	plt.plot(x, y, '-', label = label, linestyle = '--', marker = 'o')
	for xy in zip(x, y):
		plt.annotate('%.2f' % xy[1], xy = xy, textcoords = 'data')

def drawDiagram():
	plt.xlabel('iterations')
	plt.ylabel('|x - x*|')

	plt.legend(bbox_to_anchor = (0.0, 1.02, 1.0, .102), loc = 3,
		ncol = 2, mode = "expand")

	plt.show()