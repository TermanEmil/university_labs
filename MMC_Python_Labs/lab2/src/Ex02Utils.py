from MyLib import *

class PlotData:
	def __init__(self):
		self.iterations = []
		self.labels = []

	def __str__(self):
		return str({"iterations": self.iterations, "labels": self.labels})

def drawBarGraph(pltDataLst, functionNames):
	index = np.arange(len(functionNames))
	barWidth = 0.1
	barColors = ['m', 'cyan', 'orange', 'red', 'purple']

	for i in range(len(pltDataLst[0].iterations)):
		vals = [pltData.iterations[i] for pltData in pltDataLst]
		plt.bar(index + barWidth * i, vals, barWidth,
			color = barColors[i], label = pltDataLst[0].labels[i])

	plt.ylabel('iterations')
	plt.xticks(index + barWidth * 2, functionNames)
	plt.tight_layout(rect=[0, 0, 1, 0.85])
	plt.legend(bbox_to_anchor=(0, 1.2, 1, 0), loc = "upper left",
		mode = "expand", borderaxespad=False, ncol=3)

def normF(x):
	return x**3 - 3 * x**2 + 3 * x - 1

def reversedOrderF(x):
	return -1 + 3 * x - 3 * x**2 + x**3

def nestedForm(x):
	return -1 + x * (3 + x * (-3 + x))