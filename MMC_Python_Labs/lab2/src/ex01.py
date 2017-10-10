from MyLib import *

def		myFunction(x):
	return x ** (1.0 / 2) - np.e ** (-x)

toler = 10.0 ** -4
sol = 0.4263027510068627679

(x, xVals) = bisection(0, 1.2, toler, myFunction, verbose = True, sol = sol)
plotDiagram(xVals, sol, "Bisection")

(x, xVals) = newton(0.6, toler, myFunction, verbose = True, sol = sol)
plotDiagram(xVals, sol, "Newton")

(x, xVals) = simplifNewton(0.6, toler, myFunction, verbose = True, sol = sol)
plotDiagram(xVals, sol, "Simplif Newton")

(x, xVals) = secant(0.6, 1.0, toler, myFunction, verbose = True, sol = sol)
plotDiagram(xVals, sol, "Secant")

drawDiagram()