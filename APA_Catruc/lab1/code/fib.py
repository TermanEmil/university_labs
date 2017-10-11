import matplotlib.pyplot as plt
import numpy as np

def	fib1(n):
	global iterations

	iterations += 1
	if n < 2:
		return n
	else:
		return fib1(n - 1) + fib1(n - 2)

def fib2(n):
	global iterations

	i = 1
	j = 0
	for _ in range(n):
		j = i + j
		i = j - i
		iterations += 1
	return j

def fib3(n):
	global iterations

	i = 1
	j = 0
	k = 0
	h = 1
	while n > 0:
		if n % 2 == 1:
			t = j * h
			j = i * h + j * k + t
			i = i * k + t
		t = h * h
		h = 2 * k * h + t
		k = k * k + t
		n = int(n / 2)
		iterations += 1
	return j

def fib4(n):
	global iterations

	fibVals = [0] * (n + 2)
	fibVals[0] = 0
	fibVals[1] = 1
	for i in range(2, n + 1):
		fibVals[i] = fibVals[i - 1] + fibVals[i - 2]
		iterations += 1
	return fibVals[n]

def plotResults(f, n, title = None, xlabel = "n",
		ylabel = "iterations", iterDiv = 1, pltLabel = None):

	global iterations

	xPltData = []
	yPltData = []

	for i in range(n):
		iterations = 0
		f(i)

		xPltData += [i]
		yPltData += [iterations / iterDiv]

	if title != None:
		plt.title(title)

	if iterDiv != 1:
		ylabel += " (x{})".format(iterDiv)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.plot(xPltData, yPltData, label = pltLabel)

iterations = 0

plt.figure(1)
plotResults(fib1, 30, "Fib1", iterDiv = 1000)

plt.figure(2)
plotResults(fib2, 100, "Fib2")

n = 1000
plt.figure(3)
plotResults(fib3, n, "Fib3", pltLabel = "Fib3")

#Plot log_2
x = range(1, n)
y = np.log2(x)
plt.plot(x, y, label = "log2 (n)")
plt.legend(bbox_to_anchor=(1, 0.2))

plt.figure(4)
plotResults(fib4, 1000, "Fib4")

plt.figure(5)
n = 10
plotResults(fib1, n, pltLabel = "Fib1")
plotResults(fib2, n, pltLabel = "Fib2")
plotResults(fib3, n, pltLabel = "Fib3")
plotResults(fib4, n, pltLabel = "Fib4")
plt.legend(bbox_to_anchor=(0.3, 1))

plt.figure(6)
n = 100
# plotResults(fib1, n, pltLabel = "Fib1")
plotResults(fib2, n, pltLabel = "Fib2")
plotResults(fib3, n, pltLabel = "Fib3")
plotResults(fib4, n, pltLabel = "Fib4")
plt.legend(bbox_to_anchor=(0.3, 1))

plt.show()