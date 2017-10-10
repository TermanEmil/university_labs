from MyLib import *
from Ex02Utils import *

#Initialization
vrbs = True

toler = 10.0 ** -4
sol = 1

functions = [normF, reversedOrderF, nestedForm]
functionNames = [f.__name__ for f in functions]

intervals = [(0, 1.5), (0.2, 2.0), (0.6, 1.1), (-100, 100)]
guesses = [-10, 0, 1.1, 1.0001]
x1Guesses = [10, 0.6, 0.9, 0.999]

nSecantVals = min(len(guesses), len(x1Guesses))
secantIntervals = [(intervals[i][0], x1Guesses[i]) for i in range(nSecantVals)]

barPlotData = {
	"bis": [],
	"nwt": [],
	"sNwt": [],
	"sec": []
}

def printVals(label, x, sol, iterations):
	toPrintFormat = "%s: %.20f |x - x*| = %.20f iterations: %-3d"
	toPrintFormat = "\t\t" + toPrintFormat
	print(toPrintFormat % (label, x, np.fabs(x - sol), iterations))

#Iteration through all functions
for f in functions:
	print("---> ", f.__name__, " <---")

	# Bisection Method
	bisPltData = PlotData()
	for (xMin, xMax) in intervals:
		print("\t> Interval: [%.2f, %.2f] <" % (xMin, xMax))
		
		(x, xVals) = bisection(xMin, xMax, toler, f, verbose = vrbs, sol = sol)
		printVals("Bis", x, sol, len(xVals))

		bisPltData.iterations.append(len(xVals))
		bisPltData.labels.append("[{}, {}]".format(xMin, xMax))
	barPlotData['bis'].append(bisPltData)

	# Newton and Simplified Newton Method
	nwtPltData, sNwtPltData = PlotData(), PlotData()
	for guess in guesses:
		print("\t> guess = %f <" % guess)

		barLabel = "x0 = {}".format(guess)

		(x, xVals) = newton(guess, toler, f, verbose = vrbs, sol = sol)
		printVals("Newton", x, sol, len(xVals))
		nwtPltData.iterations.append(len(xVals))
		nwtPltData.labels.append(barLabel)

		(x, xVals) = simplifNewton(guess, toler, f, verbose = vrbs, sol = sol)
		printVals("Simplified Newton", x, sol, len(xVals))
		sNwtPltData.iterations.append(len(xVals))
		sNwtPltData.labels.append(barLabel)
	barPlotData["nwt"].append(nwtPltData)
	barPlotData["sNwt"].append(sNwtPltData)

	# Secant method
	secPltData = PlotData()
	for (x0, x1) in secantIntervals:
		print("\t> x0 = %.2f x1 = %.2f <" % (x0, x1))

		(x, xVals) = secant(x0, x1, toler, f, verbose = vrbs, sol = sol)
		printVals("Secant", x, sol, len(xVals))
		secPltData.iterations.append(len(xVals))
		secPltData.labels.append("[{}, {}]".format(x0, x1))

	barPlotData["sec"].append(secPltData)

#Plot
figNames = ["Bisection", "Newton", "Simplified Newton", "Secant"]
keys = ["bis", "nwt", "sNwt", "sec"]

for i in range(len(keys)):
	fig = plt.figure(i)
	fig.suptitle(figNames[i])
	drawBarGraph(barPlotData[keys[i]], functionNames)

plt.show()