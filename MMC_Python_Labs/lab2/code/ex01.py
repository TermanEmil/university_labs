import numpy as np
import matplotlib.pyplot as plt

#My functions
from lib.bisection import *
from lib.newton import *
from lib.simplifiedNewton import *
from lib.secant import *
from lib.myUtils import _plotResults

def		myFunction(x):
	return x ** (1.0 / 2) - np.e ** (-x)

def		showResultsInOneFigure(plt_Bis, plt_Nwt, plt_NwtS, plt_Sec, solution):
	plt.xlabel("iterations")
	plt.ylabel("abs error")

	_plotResults(plt_Bis, solution, "Bisection")
	_plotResults(plt_Nwt, solution, "Newton")
	_plotResults(plt_NwtS, solution, "Newton Simplified")
	_plotResults(plt_Sec, solution, "Secant")

	plt.legend(bbox_to_anchor = (0.0, 1.02, 1.0, .102), loc = 3,
		ncol = 2, mode = "expand")

	plt.show()

tolerance = 10.0 ** -4

(sol_Bis, plt_Bis) = bisectionMethod(0, 1.2, tolerance, myFunction)
(sol_Nwt, plt_Nwt) = newtonMethod(0.6, tolerance, myFunction)
(sol_NwtS, plt_NwtS) = simplifiedNewtonMethod(0.6, tolerance, myFunction)
(sol_Sec, plt_Sec) = secantMethod(0.6, 1, tolerance, myFunction)

solution = bisectionMethod(0, 1.2, 10.0 ** -14, myFunction, False)[0]

showResultsInOneFigure(plt_Bis, plt_Nwt, plt_NwtS, plt_Sec, solution)

#At ex3, Aitken extraploation
#correcion at ex3: g(x) = x(c - 1 - cx)