import numpy as np
import matplotlib.pyplot as plt

#My functions
from lib.bisection import *
from lib.newton import *
from lib.simplifiedNewton import *
from lib.secant import *
from lib.myUtils import _plotResults

def		normF(x):
	return x**3 - 3 * x**2 + 3 * x - 1

def		reversedOrderF(x):
	return -1 + 3 * x - 3 * x**2 + x**3

def		nestedForm(x):
	return -1 + x * (3 + x * (-3 + x))

def		tryFunction(f, tolerance, label, plotResults = False):
	print("<----- %s ----->" % (label))

	(sol_Bis, plt_Bis) = bisectionMethod(0, 1.2, tolerance, f)
	(sol_Nwt, plt_Nwt) = newtonMethod(-10, tolerance, f)
	(sol_NwtS, plt_NwtS) = simplifiedNewtonMethod(0.6, tolerance, f)
	(sol_Sec, plt_Sec) = secantMethod(0.6, 1, tolerance, f)	
	print ""

	if plotResults: 
		solution = bisectionMethod(0, 1.2, 10.0 ** -14, f, False)[0]
		showResultsInOneFigure(plt_Bis, plt_Nwt, plt_NwtS, plt_Sec, solution)

tolerance = 10.0 ** -6

print "- Normal form:"
print "-- [0, 1.5]"
bisectionMethod(0, 1.5, tolerance, normF)
print "-- [0.2, 2.0]"
bisectionMethod(0.2, 2.0, tolerance, normF)
print "-- [0.6, 1.1]"
bisectionMethod(0.6, 1.1, tolerance, normF)




# tryFunction(normF, tolerance, "Normal Form", showPlot)
# tryFunction(reversedOrderF, tolerance, "Reversed order ", showPlot)
# tryFunction(nestedForm, tolerance, "Nested form", showPlot)