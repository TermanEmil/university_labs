from quickSort import *
from mergeSort import *
import datetime as dt
import matplotlib.pyplot as plt
import os
import pickle
import threading
import copy
import math

class myThread (threading.Thread):
	def __init__(self, fileName):
		threading.Thread.__init__(self)
		self.fileName = fileName
		self.quickT = 0
		self.mergeT = 0

	def run(self):
		print("run: " + self.fileName)
		with open(self.fileName, 'rb') as f:
			tab = pickle.load(f)
		# self.quickT = getIters(quickSort, tab)
		# self.mergeT = getIters(mergeSort, tab)
		self.mergeT = getDeltaTime(mergeSort, tab)
		self.quickT = getDeltaTime(quickSort, tab)
		print(len(tab))

def getIters(f, tab):
	newTab = [n for n in tab]
	ret = f(newTab, 0, len(newTab) - 1)
	return ret

def getDeltaTime(f, tab):
	tab = copy.copy(tab)
	startTime = dt.datetime.now()
	f(tab, 0, len(tab) - 1)
	return (dt.datetime.now() - startTime).total_seconds()

dir = "randomNumbers/"
files = os.listdir(dir)
filesAsNb = sorted([int(file) for file in files])
files = [str(nb) for nb in filesAsNb]

quickSortTimes = []
mergeSortTimes = []
points = []

threads = []

for file in files:
	with open(dir + file, 'rb') as f:
		tab = pickle.load(f)
	mergeSortTimes.append(getDeltaTime(mergeSort, tab))
	quickSortTimes.append(getDeltaTime(quickSort, tab))
	# threads.append(myThread(dir + file))
	points.append(int(file))
	print(int(file))

# for thread in threads:
# 	thread.start()

# for thread in threads:
# 	thread.join()
# 	quickSortTimes.append(thread.quickT)
# 	mergeSortTimes.append(thread.mergeT)

# print(mergeSortTimes)
plt.plot(points, mergeSortTimes, label="mergeSort")
plt.plot(points, quickSortTimes, label="quickSort")

nLogN = [(x * math.log(x, 2)) for x in points]
gradient = (min(mergeSortTimes)) / nLogN[0]
nLogN = [x * gradient for x in nLogN]

plt.plot(points, nLogN, label="nLogN1")

nLogN = [(x * math.log(x, 2)) for x in points]
gradient = (min(quickSortTimes)) / nLogN[0]
nLogN = [x * gradient for x in nLogN]

plt.plot(points, nLogN, label="nLogN2")

plt.legend(loc="upper left")
plt.xlabel("tab size")
plt.ylabel("t (s)")
plt.show()
