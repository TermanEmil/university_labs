from quickSort import *
from mergeSort import *
from insertionSort import *

import datetime as dt
import matplotlib.pyplot as plt
import os
import pickle
import copy
import math

def getDeltaTime(f, tab):
	startTime = dt.datetime.now()
	f(copy.copy(tab), 0, len(tab) - 1)
	return (dt.datetime.now() - startTime).total_seconds()

def getAvgDeltaTime(f, tab, n):
	x = sum(getDeltaTime(f, tab) for i in range(n))
	return x / n

dir = "randomNumbers/"
files = os.listdir(dir)
filesAsNb = sorted([int(file) for file in files])
files = [str(nb) for nb in filesAsNb]

quickSortTimes = []
mergeSortTimes = []
insertSortTimes = []

points = []

for file in files:
	with open(dir + file, 'rb') as f:
		tab = pickle.load(f)
	mergeSortTimes.append(getAvgDeltaTime(mergeSort, tab, 1))
	quickSortTimes.append(getAvgDeltaTime(quickSort, tab, 1))
	insertSortTimes.append(getAvgDeltaTime(insertionSort, tab, 1))

	points.append(int(file))
	print(int(file))
	if int(file) >= 90000:
		break

plt.plot(points, mergeSortTimes, label="mergeSort")
plt.plot(points, quickSortTimes, label="quickSort")
plt.plot(points, insertSortTimes, label="insertSort")

nLogN = [(x * math.log(x, 2)) for x in points]
gradient = (min(mergeSortTimes)) / nLogN[0]
nLogN = [x * gradient for x in nLogN]

plt.plot(points, nLogN, label="nLogN1")

nLogN = [(x * math.log(x, 2)) for x in points]
gradient = (min(quickSortTimes)) / nLogN[0]
nLogN = [x * gradient for x in nLogN]

plt.plot(points, nLogN, label="nLogN2")

gradient = (min(insertSortTimes)) / points[0] ** 2
nSqr = [x**2 * gradient for x in points]
plt.plot(points, nSqr, label="n^2")

plt.legend(loc="upper left")
plt.xlabel("tab size")
plt.ylabel("t (s)")
plt.show()
