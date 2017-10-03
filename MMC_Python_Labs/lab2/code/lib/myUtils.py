import matplotlib.pyplot as plt
import numpy as np

def		_printResults(iterations, finalSol):
	print("\tIterations: %d Sol = %f" % (iterations, finalSol))

def		_plotResults(pData, solution, name):
	x = [pair[0] for pair in pData]
	y = [(np.fabs(pair[1] - solution)) for pair in pData]

	plt.plot(x, y, '-', label = name, linestyle='--', marker='o')
